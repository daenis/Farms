import binascii
from peewee import MySQLDatabase, Field
import uuid

class UUIDFieldProper(Field):
    """
    This class was takn to resolve issues with the uuid
    checkout: https://stackoverflow.com/questions/32385337/peewee-mysql-how-to-create-a-custom-field-type-that-wraps-sql-built-ins
    """
    db_field='binary(16)'

    def db_value(self, value):
        if isinstance(value, uuid.UUID):
            return value.hex
        try:
            return uuid.UUID(value).bytes
        except:
            return value

    def python_value(self, value):
        if value is None:
            return None

        return '{}-{}-{}-{}-{}'.format(
            binascii.hexlify(value[0:4]),
            binascii.hexlify(value[4:6]),
            binascii.hexlify(value[6:8]),
            binascii.hexlify(value[8:10]),
            binascii.hexlify(value[10:16])
        )

        #return value

db = MySQLDatabase('db',
                   user='user', 
                   password='password', 
                   host='localhost', 
                   port=5050,
                   fields={'binary(16)': 'BINARY(16)'}
                )
