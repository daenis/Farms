from peewee import *
from playhouse.csv_loader import load_csv
import os
import csv
#import json

CWD = os.getcwd()

class Parser:

    @staticmethod
    def csv_to_model(model, csv_file):
        load_csv(model, csv_file)

        fields = model