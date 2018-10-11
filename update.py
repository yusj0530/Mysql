import MySQLdb

# localhost=127.0.0.1(내 주소 나다.)

try:
    # 1. db 연결
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='webdb',
        password='webdb',
        db='webdb',
        charset='utf8')

    # 2. 커서 생성
    cursor = conn.cursorct()

    # 3. SQL문 실행
    sql = '''
       update pet
        set gender='m',
            death='2018-10-04'
        where species='dog'
        '''
    count = cursor.execute(sql)
    # 4. 결과 받아오기(fetch)
    result_set= cursor.fetchall()

    # 5. 자원 정리
    cursor.close()
    conn.commit()
    conn.close()

    #결과 출력
    print(count)

    # 6. 결과 처리
except MySQLdb.Error as e:
    print('Error %d: %d' % (e.args[0], e.args[1]))