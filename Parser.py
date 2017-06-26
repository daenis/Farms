import csv
import os
from db import db
from pymysql import Binary
from Farms import Farms
from uuid import uuid4
from binascii import unhexlify

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
    def __determinate(first, second):
        cmp_first = Parser._clean_string(first)
        cmp_second = Parser._clean_string(second)
        return cmp_first == cmp_second

    def __eq__(self, other):
        return self.__determinate(self.type, other)

    def __ne__(self, other):
        return self.__determinate(self.type, other)

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
        value = value.bytes.translate(str.maketrans({'-': None}))
        return Binary(bytes)

    @staticmethod
    def csv_to_model():
        cur = db.cursor()
        with open(CWD + '/farm_data.csv', 'r') as file:
            for line in file:
                parsed = Parser(line)
                if parsed == 'Farm':
                    farm = Farms()
                    farm.create(**parsed.get_dictionary())
                    print(farm.sql_insert_statement())
                    cur.execute(farm.sql_insert_statement())
