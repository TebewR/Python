print("   SELAMAT DATANG \nDI APLIKASI INPUT NILAI")

def inputdata():
    print("\n")
p = int(input("Masukkan Nilai Pengetahuan Anda : "))
k = int(input("Masukkan Nilai Keterampilan Anda : "))
s = int(input("Masukkan Nilai Sikap Anda : "))


if p >= 75 and k >= 75 and s >= 75:
    print("LULUS BRAY")
elif p < 75 and k >= 75 and s >= 75:
    print("Nilai Pengetahuan Kurang")
elif p >= 75 and k < 75 and s >= 75:
    print("Nilai Keterampilan Kurang")
elif p >= 75 and k >= 75 and s < 75:
    print("Nilai Sikap kurang")
elif p < 75 and k < 75 and s >= 75:
    print("Nilai Pengetahuan & Keterampilan kurang")
elif p < 75 and k >= 75 and s < 75:
    print("Nilai Pengetahuan & Sikap kurang")
elif p >= 75 and k < 75 and s < 75:
    print("Nilai Keterampilan & Sikap kurang")
elif p < 75 and k < 75 and s >= 75:
    print("Nilai Keterampilan & Pengetahuan kurang")
elif p < 75 and k >= 75 and s < 75:
    print("Nilai Sikap & Pengetahuan kurang")
elif p >= 75 and k < 75 and s < 75:
    print("Nilai Sikap & Keterampilan kurang")
else:
    print("tidak lulus")

again = input("Ingin Memasukkan Nilai Lagi?[y/tdk] : ")
if again == "y" or again == "Y":
    inputdata()
else:
    exit()






