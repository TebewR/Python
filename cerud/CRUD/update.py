import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='crud_python',
)


try:
    with connection.cursor() as cursor:
        sql = "UPDATE siswa SET `nama`=%s,`umur`=%s,`sekolah`=%s WHERE `id` = %s"
        try: 
            cursor.execute(sql('masukkan nama anda', 'masukkan umur anda', 1))
            print("Berhasil Di Update")
        except:
            print("Gagall Euy")

    connection.commit()
finally:
    connection.close()