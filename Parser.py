import csv
import os
from db import db
from Farms import Farms
from uuid import uuid4
from binascii import unhexlify
from FarmersMarkets import FarmersMarkets
import re

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

    @staticmethod
    def _clean_string(string):    
        return ''.join(s.lower() for s in string.rstrip() if not s.isspace())

    @staticmethod
    def format_string(string):
        regex = re.compile('.*".*,.*".*')
        if(regex.match(string)):
            string = re.sub(',','',string,count=1)
        string = re.sub('"', '',string,count=2)
        return string

    @staticmethod
    def __determinate(first, second, third):
        cmp_first = Parser._clean_string(first)
        cmp_second = Parser._clean_string(second)
        cmp_third = Parser._clean_string(third)
        regexp = re.compile('.*(%s).*'%cmp_second, flags=re.IGNORECASE)
        return cmp_first == cmp_second or regexp.search(cmp_third)

    def __eq__(self, other):
        return self.__determinate(self.type, other, self.name)

    def __ne__(self, other):
        return self.__determinate(self.type, other, self.name)

    def get_dictionary(self):
        return {
            'uuid': self._generate_id(),
            'name': self.name,
            'street_address': self.street_address,
            'city': self.city,
            'state': self.state,
            'zip': self.zip,
            'phone': self.phone,
            'website': self.website,
            'type': self.type
        }

    @staticmethod
    def _generate_id():
        value = uuid4()
        value = value.hex.translate(str.maketrans({'-': None}))
        return value[0:16]

    @staticmethod
    def csv_to_model():
        with open(CWD + '/farm_data.csv', 'r') as file:
            cur = db.cursor()
            for line in file:
                line = Parser.format_string(line)
                sql = None
                parsed = Parser(line)
                if parsed == 'Market':
                    farmers_market = FarmersMarkets()
                    farmers_market.create(**parsed.get_dictionary())
                    sql = farmers_market.sql_insert_statement()
                elif parsed == 'Farm':
                    farm = Farms()
                    farm.create(**parsed.get_dictionary())
                    sql = farm.sql_insert_statement()
                if sql != None:
                    cur.execute(sql)
                    db.commit()
            cur.close()
        db.close()
