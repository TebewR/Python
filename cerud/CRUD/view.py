import pymysql

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'crud_python',
)

try :
    with connection.cursor() as cursor:
        sql = "SELECT `id`, `nama`, `umur`, `sekolah` FROM siswa WHERE `date` = CURDATE()"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()

            print("Nama\t\t Umur\t\t\t Sekolah ")
            print("===================================================")
            for row in result:
                print(str(row[0]) + "\t\t" + row[1] + "\t\t\t" + row[2])
        
        except:
            print("WADAW GAGAL EUY MHANK!")
           
        connection.commit()
finally:
        connection.close()