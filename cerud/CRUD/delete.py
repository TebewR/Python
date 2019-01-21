import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='crud_python',
)

try:
    with connection.cursor() as cursor:
        sql = "DELETE FROM siswa WHERE id = %s"
        try:
            cursor.execute(sql, (4,))
            print("Successfully Deleted...")
        except:
            print("Oops! Something wrong")
 
    connection.commit()
finally:
    connection.close()