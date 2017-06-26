import pymysql

db = pymysql.connect(host='localhost',
                             user='user',
                             password='password',
                             db='db',
                             port=5050,
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
                             