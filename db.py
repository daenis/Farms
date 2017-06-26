import pymysql

db = pymysql.connect(host='localhost',
                             user='user',
                             password='password',
                             db='db',
                             port=5050)
