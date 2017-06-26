class Farms:
    def __init__(self):
        self.uuid = None
        self.name = ''
        self.street_address = ''
        self.state = ''
        self.city = ''
        self.zip = ''
        self.phone = ''
        self.website = ''
        self.table = 'FARMS'

    def create(self, **kwargs):
        for field in self.__dict__:
            if field != 'table':
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
            " VALUES (\"{}\", \"{}\", \"{}\", \"{}\"," \
            " \"{}\", \"{}\", \"{}\", \"{}\");".format(
                self.table,
                self.uuid,
                self.name,
                self.street_address,
                self.state,
                self.city,
                self.zip,
                self.phone,
                self.website
            )

