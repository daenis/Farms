from peewee import *
from db import db
from playhouse.csv_loader import load_csv

class Farms(Model):
    uuid = UUIDField()
    category = CharField()
    description = CharField()
    quantity = DoubleField()
    order_number = UUIDField()

    class Meta:
        database = db

    @staticmethod
    def csv_to_model():
        #Option 1: Basic example – field names and types will be introspected:
        print(load_csv(Farms, 'farm_data.csv'))

        #Option 2: Specifying fields:
        #fields = [UUIDField(), CharField(), CharField(), DoubleField(), UUIDField()]
        #field_names = ['uuid', 'category', 'description', 'quantity', 'order_number']
        #Farmers = load_csv(db, 'farm_data.csv', fields=fields, field_names=field_names)

#print