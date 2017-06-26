class Farms:
    """__slots__ = [
        'uuid',
        'name',
        'street_address',
        'state',
        'city',
        'zip',
        'phone',
        'website',
        '__table'
    ]"""
    def __init__(self):
        self.uuid = None
        self.name = ''
        self.street_address = ''
        self.state = ''
        self.city = ''
        self.zip = ''
        self.phone = ''
        self.website = ''
        self.__table = 'FARMS'

    def create(self, **kwargs):
        for field in self.__dict__:
            if field != '_Farms__table':
                print(field)
                self.__dict__[field] = kwargs[field]
    
    def sql_insert_statement(self):
        return "INSERT INTO {} (" \
            "`uuid`," \
            "`name`," \
            "`street_address`," \
            "`state`," \
            "`city`," \
            "`zip`," \
            "`phone`," \
            "`website`" \
            ")" \
            " VALUES ({}, \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\");".format(
                self.__table,
                self.uuid,
                self.name,
                self.street_address,
                self.state,
                self.city,
                self.zip,
                self.phone,
                self.website
            )

