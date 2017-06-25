from binascii import a2b_uu, b2a_hex, hexlify, unhexlify
from peewee import MySQLDatabase, Field, SelectQuery, fn
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
        print(value.urn[9:])
        if value is None:
            return None
        print(len(value.urn[9:].encode('utf8')))
        return value.urn[9:]

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
