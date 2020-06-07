"""

Your task is to gather data from the Internet,
parse it and save to a csv file

To run the file you can use your ide or terminal:
python3 -m main gather <team_name>
python3 -m main parse <team_name>
python3 -m main stats <team_name>

The logging package helps you to better track how the processes work
It can also be used for saving the errors that arise

"""

import sys
import logging
import datetime
import pandas as pd

from scraper import Scraper
from storage import Persistor
from parser import Parser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


SCRAPPED_FILE = f'scrapped_data_{sys.argv[2]}'
TABLE_FORMAT_FILE = f'data_{sys.argv[2]}.csv'


def gather():
    print('here')
    logger.info("gather")
    storage = Persistor(SCRAPPED_FILE)
    scrapper = Scraper(storage)
    for year in range(1903, int(datetime.datetime.now().year)):
        scrapper.scrape(year)


def parse():
    # parse gathered data and save as csv

    logger.info("parse")
    storage = Persistor(SCRAPPED_FILE)
    parser = Parser()
    for year in range(1903, int(datetime.datetime.now().year)):
        raw_data = storage.read_raw_data(year)
        parsed_file = parser.parse_object(raw_data)
        storage.append_data(parsed_file)
    storage.save_csv(TABLE_FORMAT_FILE)


def stats():
    """ If you have time, you can calculate some statistics on the data gathered """
    logger.info("stats")

    if len(sys.argv) <= 1:
        print('Please give the name of the football team via www.worldfootball.net')

    try:
        df = pd.read_csv (f'output/data_{sys.argv[2]}.csv') 
    except:
        print (f'\
        There is not data with your football team name ({sys.argv[2]}), \n\
        please run the following commands with your team name befor this step, \n\
        python3 -m main gather <team_name> \n\
        python3 -m main parse  <team_name> \n\
        then call this option      \
        ')
        exit()
    
    
    mean = df['Scored'].mean()
    sum = df['Scored'].sum()
    max = df['Scored'].max()
    count = df['Scored'].count()
    std = df['Scored'].std()
    var = df['Scored'].var()
    meanm = df['Missed'].mean()
    summ = df['Missed'].sum()
    maxm =  df['Missed'].max()
    stdm = df['Missed'].std()
    varm = df['Missed'].var()

    countOfWins = df[df['Scored'] > df['Missed']].count()['Date']
    countOfDefeats = df[df['Scored'] < df['Missed']].count()['Date']

    def f(x):                        
        d={}
        d['Scored_sum'] = x['Scored'].sum()
        d['Missed_sum'] = x['Missed'].sum()
        d['Number_of_wins'] = (x['Scored'] - x['Missed']>0).sum()
        d['Number_of_defeats'] = (x['Scored'] - x['Missed']<0).sum()
        d['Number_of_draws'] = (x['Scored'] - x['Missed']==0).sum()
        d['Wins_Percentage(%)'] = d['Number_of_wins'] * 100 / x['Scored'].count()
        return pd.Series(d, index=['Scored_sum','Missed_sum','Number_of_wins','Number_of_defeats','Number_of_draws','Wins_Percentage(%)'])
    
    df.groupby(['Opponent']).apply(f).to_csv(f'output/stats_{sys.argv[2]}.csv',encoding='utf-8')

    print (f'\
#########################################################################\n\
#########################################################################\n\
#########################################################################\n\
Team Name = {sys.argv[2]} \n\
Average of scored goals = {mean}\n\
Average of missed goals = {meanm}\n\
Total sum of scored goals = {sum}\n\
Total sum of missed goals = {summ}\n\
The record of scored goals = {max}\n\
The record of missed goals = {maxm}\n\
Standart deviation of scored goals = {std}\n\
Standart deviation of missed goals = {stdm}\n\
Variance of scored goals = {var}\n\
Variance of missed goals = {varm}\n\
The count of played games = {count}\n\
#########################################################################\n\
#########################################################################\n\
#########################################################################\n\
\n\n\n\
The stats of {sys.argv[2]} against each team that he played you can see here output/stats_{sys.argv[2]}.csv\n\
        ')

        
    # Your code here
    # Load pandas DataFrame and print to stdout different statistics about the data.
    # Try to think about the data and use as different methods applicable to DataFrames.
    # Ask yourself what would you like to know about this data (most frequent word, average price, e.t.c.)


if __name__ == '__main__':
    """
    What does the line above mean
    https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    """
    logger.info("Work started")

    if sys.argv[1] == 'gather':
        gather()

    elif sys.argv[1] == 'parse':
        parse()
    elif sys.argv[1] == 'stats':
        stats()
    logger.info("work ended")
