import csv
import os
from db import db
from peewee import *
from playhouse.csv_loader import load_csv

CWD = os.getcwd()

class Parser:
    """Parse the CSV and convert to model"""
    # creates member scopes for the instance
    # saves memory rather than standard dict
    __slots__ = [
        'name',
        'street_address',
        'state',
        'city',
        'zip',
        'phone',
        'website',
        'type'
    ]
    def __init__(self, string):
        values = string.split(',')
        self.name = values[0]
        self.street_address = values[1]
        self.city = values[2]
        self.state = values[3]
        self.zip = values[4]
        self.phone = values[5]
        self.website = values[6]
        self.type = values[7]

    def __lt__(self, other):
        pass
    def __le__(self, other):
        pass
    def __eq__(self, other):
        pass
    def __ne__(self, other):
        pass
    def __gt__(self, other):
        pass
    def __ge__(self, other):
        pass


    @staticmethod
    def csv_to_model():
        db.connect()
        with open(CWD + '/farm_data.csv', 'r') as file:
            for line in file:
                print(line)
