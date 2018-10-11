
#pet table에 CRUD 함수를 정의한 모듈
import MySQLdb

#connect
import config


def connect():
    try:
        conn = MySQLdb.connect(
            host=config.CONNECTION[ 'host' ],
            port=config.CONNECTION[ 'port' ],
            user=config.CONNECTION[ 'user' ],
            password=config.CONNECTION[ 'password' ],
            db=config.CONNECTION[ 'db' ],
            charset=config.CONNECTION[ 'charset' ])
        return  conn

    except MySQLdb.Error as e:
        print('Error %d: %d' % (e.args[0], e.args[1]))
        return None


#CRU(D)
def delete(name):
    try:
        conn = connect()

        # 2. 커서 생성
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)

        # 3. SQL문 실행
        sql = '''
          delete
              from pet
              where name='%s'
              ''' % name
        count = cursor.execute(sql)

        # 4. 자원 정리

        cursor.close()
        conn.commit()
        conn.close()

        # 5. 결과 처리
        return count >= 1
    except MySQLdb.Error as e:
            print('Error %d: %d' % (e.args[0], e.args[1]))
            return False


#CR(U)D
def update(name):
    try:
        conn=connect()

        cursor = conn.cursor(MySQLdb.cursors.DictCursor)

        sql='''
        update pet
            set name='하얀마음 백구'
            where name='%s'
            ''' % name
        count=cursor.execute(sql)

        cursor.close()
        conn.commit()
        conn.close()

        return count == 1
    except MySQLdb.Error as e:
        print('Error %d: %d' % (e.args[0], e.args[1]))
        return False


#C(R)UD

def fetchByName(name):
    try:
        conn = connect()

        # 2. 커서 생성
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)

        # 3. SQL문 실행
        sql = '''
          select *
              from pet
              where name='%s'
              ''' % name
        cursor.execute(sql)

    # 4. 자원 정리

        row = cursor.fetchone()
        cursor.close()

        conn.close()

        # 5. 결과 처리
        return row
    except MySQLdb.Error as e:
            print('Error %d: %d' % (e.args[0], e.args[1]))
            return False

def fetchall():
    try:
        conn=connect()
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)

        #name='''select name from pet'''
        sql =''' select name
                from pet
                '''
        cursor.execute(sql)

        rows = cursor.fetchall()
        # for row in rows:
        #     if row is None:
        #         break
        #     else :
        #         print(row)
        print(rows)

        cursor.close()
        conn.close()
    except MySQLdb.Error as e:
        print('Error %d: %d' % (e.args[0], e.args[1]))
        return  False


#(C)RUD
def insert(pet):
    try:
        conn= connect()

    # 2. 커서 생성
        cursor = conn.cursor()

    # 3. SQL문 실행
        sql = '''
        insert
	        into pet
        values ('%s', '%s', '%s','%s','%s','0000-00-00')
        '''% (pet['name'], pet['owner'], pet['species'], pet['gender'],pet['birth'])
        count = cursor.execute(sql)

   # 4. 자원 정리
        cursor.close()
        conn.commit()
        conn.close()

       # 5. 결과 처리
        return count == 1
    except MySQLdb.Error as e:
        print('Error %d: %d'% (e.args[0], e.args[1]))