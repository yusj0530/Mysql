import MySQLdb
#localhost=127.0.0.1(내 주소 나다.)

try:
    # 1. db 연결
   conn= MySQLdb.connect(
        host='localhost',
        port=3306,
        user='webdb',
        password='webdb',
        db='webdb',
        charset='utf8')

    # 2. 커서 생성
   cursor = conn.cursor()

    # 3. SQL문 실행
   sql = '''
        insert
	        into pet(owner, name, species, gender, birth)
        values ('찬이', '마음이2', 'dog','m','1994-02-10');
        '''
   count = cursor.execute(sql)

   # 4. 자원 정리
   cursor.close()
   conn.commit()
   conn.close()

   # 5. 결과 처리
   print(count)

except MySQLdb.Error as e:
        print('Error %d: %d'% (e.args[0], e.args[1]))