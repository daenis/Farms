from binascii import a2b_uu, b2a_hex, hexlify, unhexlify
from peewee import MySQLDatabase, BlobField, SelectQuery, fn
from uuid import UUID
import string
import chardet
from pymysql import Binary

class UUIDFieldProper(BlobField):
    """
    This class was takn to resolve issues with the uuid
    checkout: 
    https://stackoverflow.com/questions/32385337/peewee-mysql-how-to-create-a-custom-field-type-that-wraps-sql-built-ins
    https://github.com/coleifer/peewee/issues/788
    """
    db_field='binary(16)'

    def db_value(self, value):
        if value is None:
            return None
        print(chardet.detect(value.bytes))
        value = value.hex.translate(str.maketrans({'-': None}))
        query = SelectQuery(self.model_class, fn.UNHEX(value).alias('unhex'))
        result = query.first()
        print(result.unhex)
        return Binary(result.unhex)

    def python_value(self, value):
        if value is None:
            return None
        query = SelectQuery(self.model_class, fn.HEX(value).alias('hex'))
        result = query.first()
        value = '{}-{}-{}-{}-{}'.format(
            result.hex[0:8],
            result.hex[8:12],
            result.hex[12:16],
            result.hex[16:20],
            result.hex[20:32]
        )
        return value

db = MySQLDatabase('db',
                   user='user', 
                   password='password', 
                   host='localhost', 
                   port=5050,
                   fields={'binary(16)': 'BINARY(16)'}
                )
