from peewee import *
from db import db

class Farmers_Market(Model):
    uuid = UUIDField(primary_key=True)
    city = CharField()
    email = CharField()
    phone = CharField()
    street_address = CharField()
    website = CharField()
    state = CharField()
    contact = UUIDField()

    class Meta:
        database = db
        db_table = 'FARMERS_MARKET'
        auto_increment = False
