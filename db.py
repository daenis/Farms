from binascii import b2a_hex, hexlify, unhexlify
from peewee import MySQLDatabase, Field
from uuid import UUID

class UUIDFieldProper(Field):
    """
    This class was takn to resolve issues with the uuid
    checkout: 
    https://stackoverflow.com/questions/32385337/peewee-mysql-how-to-create-a-custom-field-type-that-wraps-sql-built-ins
    https://github.com/coleifer/peewee/issues/788
    """
    db_field='binary(16)'

    def db_value(self, value):
        return ''.join('%02x' % v for v in value)

    def python_value(self, value):
        bytes = []

        hexStr = ''.join( value.split(" ") )

        for i in range(0, len(hexStr), 2):
            bytes.append( chr( int (hexStr[i:i+2], 16 ) ) )

        return ''.join( bytes )


db = MySQLDatabase('db',
                   user='user', 
                   password='password', 
                   host='localhost', 
                   port=5050,
                   fields={'binary(16)': 'BINARY(16)'}
                )
