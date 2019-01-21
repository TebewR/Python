import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='crud_python',
)

nama = input("Masukkan Nama Anda : ")
umur = input("Masukkan Umur Anda : ")
sekolah = input("Masukkan Asal Sekolah Anda : ")
date = input("Masukkan (yyyy-mm-dd)  : ")

try:
    with connection.cursor() as cursor:
        sql = "INSERT INTO siswa (`nama`, `umur`, `sekolah`, `date`) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(sql,(nama, umur, sekolah, date))
            print('Berhasil Diinput Brow!')
        except:
            print("Gagal Euy!")

    connection.commit()
finally:
    connection.close()