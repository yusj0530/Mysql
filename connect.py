import MySQLdb
#localhost=127.0.0.1(내 주소 나다.)

try:
    MySQLdb.connect(
        host='localhost',
        port=3306,
        user='webdb',
        password='webdb',
        db='webdb',
        charset='utf8')
    print('connected successfully')
except MySQLdb.Error as e:
        print('Error %d: %d'% (e.args[0], e.args[1]))
