print("                       Selamat Datang DI Pemecahan Uang SkuyyyyyyyLivingssssss")
uang = int(input ("Masukan uang anda : "))
d = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]

for x in range(11):
    i = 0
    while uang >= d[x]:
        uang = uang - d[x]
        i = i+1
        if i>0:
            print("Uang %a sebanyak %a lembar" %(d[x],i))
        else:
            print("gagal")