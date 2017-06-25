from binascii import hexlify
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
        if isinstance(value, UUID):
            return hexlify(value.bytes)
        try:
            return hexlify(UUID(value).bytes)
        except:
            return value

    def python_value(self, value):
        if value is None:
            return None

        return '{}-{}-{}-{}-{}'.format(
            hexlify(value[0:4]),
            hexlify(value[4:6]),
            hexlify(value[6:8]),
            hexlify(value[8:10]),
            hexlify(value[10:16])
        )

db = MySQLDatabase('db',
                   user='user', 
                   password='password', 
                   host='localhost', 
                   port=5050,
                   fields={'binary(16)': 'BINARY(16)'}
                )
