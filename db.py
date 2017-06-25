from binascii import b2a_hex, hexlify, unhexlify
from peewee import MySQLDatabase, BlobField
from uuid import UUID

class UUIDFieldProper(BlobField):
    """
    This class was takn to resolve issues with the uuid
    checkout: 
    https://stackoverflow.com/questions/32385337/peewee-mysql-how-to-create-a-custom-field-type-that-wraps-sql-built-ins
    https://github.com/coleifer/peewee/issues/788
    """
    db_field='binary(16)'

    def db_value(self, value):
        if not isinstance(value, UUID):
            value = UUID(value)
        parts = str(value).split("-")
        reordered = ''.join([parts[2], parts[1], parts[0], parts[3], parts[4]])
        value = unhexlify(reordered)
        return super(UUIDFieldProper, self).db_value(value)

    def python_value(self, value):
        u = b2a_hex(value)
        value = u[8:16] + u[4:8] + u[0:4] + u[16:22] + u[22:32]
        return UUID(value)

db = MySQLDatabase('db',
                   user='user', 
                   password='password', 
                   host='localhost', 
                   port=5050,
                   fields={'binary(16)': 'BINARY(16)'}
                )
