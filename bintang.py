#membuat bintang menggunakan perulangan
sisi_1=10
print("awal while")
count=1
spasi=int(sisi_1/2)

while True:
    if (count%2):
        #print jika ganjil
        print(" "*spasi,"+"*count)
        spasi-=1
        count+=1
    else:
        count+=1
        continue

    if count>sisi_1:
        break
print("akhir while")
#membuat bintang menggunakan perulangan
sisi=10
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    if count > sisi:
        break
while True:
    if (count%2): 
        spasi += 1
        print(" "*spasi,"+"*count)
        count -= 1
    else:
        count -= 1
    if count == 0:
        break
#membuat bintang menggunakan perulangan
sisi_2=1
print("awal while")
count=10
spasi=int(sisi_2/2)

while True:
    if (count%2):
        spasi+=1
        #print jika ganjil
        print(" "*spasi,"+"*count)
        count -= 1
    else:
        count -= 1
    if count == 0:
        break
print("akhir while")