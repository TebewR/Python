import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  db = 'crud_python',
)

print("Berhasil Connect Cuy!")