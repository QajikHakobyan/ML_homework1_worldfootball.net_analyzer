import logging
import requests
import sys
logger = logging.getLogger(__name__)


class Scraper:

    def __init__(self, storage):
        self.storage = storage

    def checkUrl(self, response):
        initUrl = f'https://www.worldfootball.net'
        initResponse = requests.get(initUrl)
        initResponse.encoding = 'utf-8'

        if response.text == initResponse.text:
            return False
        return True

    def scrape(self, year):
        """ Gives the text from ACA website """

    
        url = f'https://www.worldfootball.net/teams/{sys.argv[2]}/{year}/3/'
        response = requests.get(url) 
        response.encoding = 'utf-8'

        if not response.ok:
            # log the error
            logger.error(response.text)
    
        else:
            if not self.checkUrl(response):
                print("You give the wrong name of football team, please check your teamname in www.worldfootball.net")
                exit()
            # Note: here json can be used as response.json
            data = response.text

            # save scraped objects here
            # you can save url to identify already scrapped objects
            self.storage.save_raw_data(year,data)

