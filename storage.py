import os
import sys
import os.path
import csv
from os import path
from lxml import html

class Persistor:

    data = []

    def __init__(self, dir = None):
        self.dir = dir
        try:
            if dir != None and path.exists(dir) != True:
                os.mkdir(dir)
        except OSError:
            print ("Creation of the directory %s failed" % dir)
        else:
            print ("Successfully created the directory %s " % dir)

    def read_raw_data(self, fileName):  
        file = open(f"{self.dir}/{fileName}.html", "r")
        return file.read()

    def save_raw_data(self, fileName ,data):
        file = open(f"{self.dir}/{fileName}.html", "w")
        file.write(data)
        file.close()

    def save_csv(self, TABLE_FORMAT_FILE):
        if not path.exists("output"):
            os.makedirs("output")
        file = open(f'output/{TABLE_FORMAT_FILE}', "w+")
        writer = csv.DictWriter(file, fieldnames=["Date", "Time", "Place", "Opponent", "Scored" ,"Missed"])
        writer.writeheader()
        for d in self.data:
            file.write(str(d) + '\n')
        file.close()

    def append_data(self, data):
        self.data.extend(data)

