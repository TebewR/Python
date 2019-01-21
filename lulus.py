p = int(input("Pengetahuan : "))
k = int(input("Keterampilan : "))
s = int(input("Sikap : "))

if p and k and s < 75:
    print("Belum Kompeten")
else:
    print("Kompeten")    