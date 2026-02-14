a=15
b=10
pendek=15

print("nilai a adalah: ",a)
print("nilai b adalah: ",b)
print("nilai pendek adalah: ",pendek)

nilai_z=1000
niali_x=1629
jumlah91=100000002020

print("nilai a = ",a)
a=801
print("nilai a = ",a)

print("nilai a = ",a)
a=801
print("nilai a = ",a)
print("nilai b = ",b)
b=801
print("nilai b = ",b)

#ini adalah data integer
data_string=111625
print("data : ",data_string)
print("-bertipe : ",type(data_string))
#ini adalah data float
data_float=13.298
print("data : ",data_float)
print("-bertipe : ",type(data_float))
#ini adalah data string
data_string="andi bachdar dd"
print("data : ",data_string)
print("-bertipe : ",type(data_string))
#ini adalah data bolean
data_boolean=True
print("data : ",data_boolean)
print("-bertipe : ",type(data_boolean))

#tipe data khusus
#tipe complex
data_complex=complex(5,7)
print("data : ",data_complex)
print("-bertipe : ",type(data_complex))
from ctypes import c_double
#tipe complex
data_c_double=c_double(50.1777)
print("data : ",data_c_double)
print("-bertipe : ",type(data_c_double))
#materi casting
#casting adsalah mengubah suatu variable ke tipe data lain
print("====integer====")
data_int=9881;
print("data = ",data_int,",type= ",type(data_int))
#mengubah tipe data/conversi tipe data
data_string=str(data_int)
data_float=float(data_int)
data_bool=bool(data_int)
print("data = ",data_string,",type= ",type(data_string))
print("data = ",data_float,",type= ",type(data_float))
print("data = ",data_bool,",type= ",type(data_bool))

print("====float====")
data_float=9881;
print("data = ",data_float,",type= ",type(data_float))
#mengubah tipe data/conversi tipe data
data_string=str(data_float)
data_int=int(data_float)
data_bool=bool(data_float)
print("data = ",data_string,",type= ",type(data_string))
print("data = ",data_int,",type= ",type(data_int))
print("data = ",data_bool,",type= ",type(data_bool))

print("====string====")
data_str=9881;
print("data = ",data_str,",type= ",type(data_str))
#mengubah tipe data/conversi tipe data
data_float=float(data_str)
data_int=int(data_str)
data_bool=bool(data_str)
print("data = ",data_float,",type= ",type(data_float))
print("data = ",data_int,",type= ",type(data_int))
print("data = ",data_bool,",type= ",type(data_bool))
print("====boolean====")

data_bool=9881;
print("data = ",data_bool,",type= ",type(data_bool))
#mengubah tipe data/conversi tipe data
data_float=float(data_bool)
data_int=int(data_bool)
data_str=str(data_str)
print("data = ",data_float,",type= ",type(data_float))
print("data = ",data_int,",type= ",type(data_int))
print("data = ",data_str,",type= ",type(data_str))
#memasukkan input kepada variable dan menkonvertnya ke tipe data yang kita inginkan
#data yang dimasukkan string
data=input("masukkan nama anda : ")
print("data adalah : ",data,"type = ",type(data))
#data yang dimasukkan int atau float
angka_int=int(input("masukkan data integer : "))
print("angka yang kamu masukkan adalah: ",angka_int,"type = ",type(angka_int))
#data yang anda masukkan float
data_float=float(input("masukkan data float: "))
print("data float yang anda masukkan: ",data_float,"type: ",data_float)
#data yang anda masukkan bollean
data_bool=bool(int(input("masukkan data boolean: ")))
print("data bollean yang anda masukkan: ",data_bool,"type: ",data_bool)

#operasional aritmatika
a=15
b=13
#operasi penjumlahan +
hasil=a+b
print(a,"+",b,"=",hasil)
#operasi pengurangan -
hasil=a-b
print(a,"-",b,"=",hasil)
#operasi perkalian *
hasil=a*b
print(a,"*",b,"=",hasil)
#operasi pembagian /
hasil=a/b
print(a,"/",b,"=",hasil)
#operasi eksponen **
hasil=a**b
print(a,"**",b,"=",hasil)
#operasi modulus %
hasil=a%b
print(a,"%",b,"=",hasil)
#operasi floor devesion //
hasil=a//b
print(a,"//",b,"=",hasil)

#operasi prioritas
"""
    1.()
    2.eksponen **
    3.perkalian dan teman temanya * / % // **
    4.pertambahan dan pengurangan + -
"""
x=5
y=4
z=3
hasil= x** y * z + x / y - y % z // x
print(x,"**",y,"*",z,"+",x,"/",y,"-",y,"%",z,"//",x,"=",hasil)
#urutan akan di prioritaskan ke penjumlahan yang di dalam kurung terlebih dahulu
hasil=x+y*z
print(x,"+",y,"*",z,"=",hasil)
#kurung akan mengambil langkah yang paling awal
hasil = (x + y) * z
print('(',x,'+',y,') * ',z,'=',hasil)

#program konversi temperatur
print("\nPROGRAM KONVERSI TEMPRATUR\n")
#celcius
celcius=float(input('Masukkan suhu dalam Celcius: '))
print('suhu yang anda masukkan adalah',celcius,'Celcius')
#fahrenheit
fahrenheit=((9/5)*celcius)+32
print('suhu dalam fahrenheit adalah',fahrenheit,'fahrenheit')
#reamur
reamur=(4/5)*celcius
print('suhu dalam reamur adalah',reamur,'reamur')
#kelvin
kelvin=celcius+273
print('suhu dalam kelvin adalah',kelvin,'kelvin')

#pr konversi kelvin ke fahrenheit
fahrenheitkonversi= (kelvin - 273.15) * 9/5 + 32
print('suhu dalam fahrenheit konversi ke kelvin adalah',fahrenheitkonversi,'fahrenheit')
#pr konversi fahrenheit ke kelvin
kelvinkonversi=(fahrenheit -32)*5/9+273.15
print('suhu dalam kelvin konversi ke fahrenheit adalah',kelvinkonversi,'kelvin')

#operasi komperasi atau true or false
# >, <, >= ,<= ,== ,!= ,is ,is not
a = 5
b = 2
 # operasi komperasi (>)
print('========= lebih dari (>)')
hasil= a > 4
print(a,'>',5,'=',hasil)
hasil= b > 4
print(b,'>',4,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
 # operasi komperasi (<)
print('========= kurang dari (<)')
hasil= a < 4
print(a,'<',5,'=',hasil)
hasil= b < 4
print(b,'<',4,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
 # operasi komperasi lebih besar sama dengan (>=)
print('========= lebih besar sama dengan (>=)')
hasil= a >= 4
print(a,'>=',5,'=',hasil)
hasil= b >= 4
print(b,'>=',4,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
 # operasi kurang sama dengan (<=)
print('========= kurang dari sama dengan (<=)')
hasil= a <= 4
print(a,'<=',5,'=',hasil)
hasil= b <= 4
print(b,'<=',4,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
 # operasi komperasi (==)
print('========= sama dengan (==)')
hasil= a == 4
print(a,'==',5,'=',hasil)
hasil= b == 4
print(b,'==',4,'=',hasil)
hasil = b == 3
print(b,'==',3,'=',hasil)
 # operasi komperasi (!=)
print('========= tidak sama dengan (!=)')
hasil= a != 4
print(a,'!=',5,'=',hasil)
hasil= b != 4
print(b,'!=',4,'=',hasil)
hasil = b != 3
print(b,'!=',3,'=',hasil)
 # operasi komperasi is sebagai komperasi identity (is) sebagai objek
print('========= identitiy (is)')
x=5
y=5
print("nilai x = ",x,"id",hex(id(x)))
print("nilai y = ",y,"id",hex(id(y)))
hasil=x is y
print('x is y =',hasil)
# operasi komperasi is sebagai komperasi identity (is) membuat object
print('========= identitiy (is)')
x=7
y=5
print("nilai x = ",x,"id",hex(id(x)))
print("nilai y = ",y,"id",hex(id(y)))
hasil=x is y
print('x is y =',hasil)
# ini adalah assigment membuat object
print('========= identitiy (is not)')
x=5
y=5
print("nilai x = ",x,"id",hex(id(x)))
print("nilai y = ",y,"id",hex(id(y)))
hasil= x is not y
print('x is y =',hasil)
# ini adalah assigment membuat object
print('========= identitiy (is not)')
x=6
y=5
print("nilai x = ",x,"id",hex(id(x)))
print("nilai y = ",y,"id",hex(id(y)))
hasil= x is not y
print('x is y =',hasil)

#operasi logika atau boleean
# not, or, and, xor
#not
print("=====NOT=====")
a=True
c= not a
print("data a = ",a)
print("-----NOT")
print("data c = ",c)
#OR(jika salah satu true maka outpunya true )
print("====OR====")
a=True
b=False
c= a or b
print(a,"OR",b," =",c)
a=True
b=True
c= a or b
print(a,"OR",b,"  =",c)
a=False
b=False
c= a or b
print(a,"OR",b,"=",c)
a=False
b=True
c= a or b
print(a,"OR",b," =",c)
# AND(jika salah satu False maka outpunya False)
print("====AND====")
a=True
b=False
c= a and b
print(a,"AND",b," =",c)
a=True
b=True
c= a and b
print(a,"AND",b,"  =",c)
a=False
b=False
c= a and b
print(a,"AND",b,"=",c)
a=False
b=True
c= a and b
print(a,"AND",b," =",c)
#XOR(akan True jika salah satu true,sisanya False )
print("====XOR====")
a=True
b=False
c= a ^ b
print(a,"XOR",b," =",c)
a=True
b=True
c= a ^ b
print(a,"XOR",b,"  =",c)
a=False
b=False
c= a ^ b
print(a,"XOR",b,"=",c)
a=False
b=True
c= a ^ b
print(a,"XOR",b," =",c)

#perpaduan logika danoperasi perbandingan

#membuat gabungan area rentan dari angka
#++++++3-------10+++++++
inputUser=float(input("masukkan angka yang bernilai\n kurang dari 3\n dan\n lebih dari 10 = "))
#++++++3
#memeriksa angka yang kamu masukkan kurang dari 3
isKurangDari = (inputUser < 3)
print("masukkan angka yang kurang dari 3 = ",isKurangDari)
#10+++++
#memeriksa angka yang kamu masukkan lebih dari 10
isLebihDari = (inputUser > 10)
print("masukkan angka yang lebih dari 10 = ",isLebihDari)
isCorrect=isKurangDari or isLebihDari
print("masukkan angka : ",isCorrect)
#membuat kasus irisan
#------3++++++10------
print("=====Irisan=====")
inputUser=float(input("masukkan angka yang bernilai\n lebih dari 3\n dan\n kurang dari 10 = "))
#------3
#memeriksa angka yang kamu masukkan kurang dari 3
isLebihDari = (inputUser > 3)
print("masukkan angka yang lebih dari 3 = ",isLebihDari)
#10-----
#memeriksa angka yang kamu masukkan lebih dari 10
isKurangDari = (inputUser < 10)
print("masukkan angka yang kurang dari 10 = ",isKurangDari)
isCorrect=isKurangDari and isLebihDari
print("masukkan angka : ",isCorrect)

#pr operator perbandingan
#1. -----0+++++5-----8+++++11------
#2. +++++0-----5+++++8-----11++++++
#kerjakan nomer 1 dulu
print("======Soal Nomor 1=====")
inputUser=float(input("masukkan angka yang bernilai\n lebih dari 0\n kurang dari 5 \nlebih dari 8 \n  dan\n kurang dari 11 = "))
#------0
#memeriksa angka yang kamu masukkan lebih dari 0 
isLebihDari0 = (inputUser > 0)
print("masukkan angka yang lebih dari 0 = ",isLebihDari0)
#5+++++
#memeriksa angka yang kamu masukkan kurang dari 5
isKurangDari5 = (inputUser < 5)
print("masukkan angka yang kurang dari 5 = ",isKurangDari5)
#8+++++
#memeriksa angka yang kamu masukkan Lebih dari 8
isLebihDari8 = (inputUser > 8)
print("masukkan angka yang lebih dari 8 = ",isLebihDari8)
#11------
#memeriksa angka yang kamu masukkan kurang dari 11
isKurangDari11 = (inputUser < 11)
print("masukkan angka yang kurang dari 11 = ",isKurangDari11)
#mengecek hasilnya
isCorrect=isLebihDari0 and isKurangDari5 or isLebihDari8 and isKurangDari11
print("masukkan angka : ",isCorrect)
#2. +++++0-----5+++++8-----11++++++
#+++++0
print("======Soal nomer 2=====")
inputUser=float(input("masukkan angka yang bernilai\n kurang dari 0\n lebih dari 5 \n kurang dari 8 \n  dan\n lebih dari 11 = "))
#soal nomer 2
isKurangDari0 = (inputUser < 0)
print("masukkan angka yang kurang dari 0 = ",isKurangDari0)
#5+++++
#memeriksa angka yang kamu masukkan kurang dari 5
isLebihDari5 = (inputUser > 5)
print("masukkan angka yang lebih dari 5 = ",isLebihDari5)
#+++++8
#memeriksa angka yang kamu masukkan Lebih dari 8
isKurangDari8 = (inputUser < 8)
print("masukkan angka yang Kurang dari 8 = ",isKurangDari8)
#11------
#memeriksa angka yang kamu masukkan kurang dari 11
isLebihDari11 = (inputUser > 11)
print("masukkan angka yang Lebih dari 11 = ",isLebihDari11)
#mengecek hasilnya
isCorrect=isKurangDari0 or isLebihDari5 and isKurangDari8 or isLebihDari11
print("masukkan angka : ",isCorrect)

#operasi bitwise, operasi biner, binary
a = 9
b = 5
#bitwise OR(|)
c = a | b
print("\n=========OR=========")
print("Nilai :",a,"binary : ",format(a,"08b"))
print("Nilai :",b,"binary : ",format(b,"08b"))
print("-----------------------------------(|)")
print("Nilai :",c,"binary :",format(c,"08b"))
#bitwise AND(&)
c = a & b
print("\n=========AND========")
print("Nilai :",a,"binary : ",format(a,"08b"))
print("Nilai :",b,"binary : ",format(b,"08b"))
print("-----------------------------------(&)")
print("Nilai :",c,"binary :",format(c,"08b"))
#bitwise XOR(^)
c = a ^ b
print("\n=========XOR========")
print("Nilai :",a,"binary : ",format(a,"08b"))
print("Nilai :",b,"binary : ",format(b,"08b"))
print("-----------------------------------(^)")
print("Nilai :",c,"binary :",format(c,"08b"))
#bitwise Not (~)
c = a ^ b
print("\n=========NOT========")
print("Nilai :",a,"binary : ",format(a,"08b"))
print("-----------------------------------(~)")
print("Nilai :",c,"binary :",format(c,"08b"))
print("-----------------------------------(~)")
d = 0b0000001001
e = 0b1111111111
print("nilai :",e^d,"binary :",format(e^d,"08b"))

#shifting
#shift righat(>>)
c = a >> b
print("\n=========>>========")
print("Nilai :",a,"binary : ",format(a,"08b"))
print("-----------------------------------(>>)")
print("Nilai :",c,"binary :",format(c,"08b"))
#shift left(<<)
c = a << b
print("\n=========<<========")
print("Nilai :",a,"binary : ",format(a,"08b"))
print("-----------------------------------(<<)")
print("Nilai :",c,"binary :",format(c,"08b"))

#operasi yang dilakukan dengan penyingkatan
#operasi dengan ditambah assigment

a=5 #adalah assigment
print("nilai a = ",a)

a += 1 # artinya a = 5 + 1
print("nilai a + = 1, nilai a menjadi",a)
a *= 5 # artinya a = 6 * 5 
print("nilai a * = 5, nilai a menjadi",a)
a -= 8 # artinya a = 30 - 8
print("nilai a - = 8, nilai a menjadi",a)
a /= 5 # artinya a = 29 /5
print("nilai a / = 5, nilai a menjadi",a)

b=10
print("\n nilai b =",b)

#modulus dan floor devision
b%=3
print("nilai a % = 3, nilai a menjadi",b)

b=10
print("\n nilai b =",b)

#modulus dan floor devision
b//=3
print("nilai a // = 3, nilai a menjadi",b)
#pangkat atau eksponen
a=5
print("\n nilai a =",a)
a **=5
print("nilai a ** = 5, nilai a menjadi",a)
#operasi bitwise
#or
c=True
print("\n nilai c = ",c)
c |=False
print("nilai c|= False, nilai c menjadi",c)
c=False
print("nilai c = ",c)
c |=False
print("nilai c|= False, nilai c menjadi",c)
#AND
c=True
print("\n nilai c = ",c)
c &=False
print("nilai c&= False, nilai c menjadi",c)
c=False
print("nilai c = ",c)
c &=False
print("nilai c&= False, nilai c menjadi",c)
#XOR
c=True
print("\n nilai c = ",c)
c ^=False
print("nilai c^= False, nilai c menjadi",c)
c=False
print("nilai c = ",c)
c ^=False
print("nilai c^= False, nilai c menjadi",c)
#geser mengeser 
d=0b00100
print("\nnilai d adalah= ",format(d,"04b"))
d >>=2
print("nilai d menjadi >>=2 ",format(d,"04b"))
d <<=3
print("nilai d menjadi <<=3 ",format(d,"04b"))

#string
data="ini adalah string"
print(data)
print(type(data))

#cara membuat string
"""
    1.membuat string dengan single code ''
    2.membuat string dengan double code ""
"""
data='menggunakan single Quote'
print(data)
data="menggunakan Double Quote"
print(data)
print('andi bahdar')
print("andi bachdar dd")
print("apakah hari ini hari minggu")
print("apakah hari ini hari jum'at")
#2 menggunakan tanda\
print("besok hari sabtu \n hari ini hari minggu \n lusa hari juma'at")
print("C:\\user\\bahdar")
#membuat string menjadi tab berjarak
print("andi bachdar\tS.KOM")
#membuat string backspace atau berdekatan
print("andi\bbahdar")
#newline
print("andi bachdar \n umur 25\n asal kendari") #LF (line Feeed)unix (max,linux dkk)
print("andi bachdar dd\r asal kendari") #CR (Carriage return)
print("andi bachdar dd\r\n asal kendari sulawesi tenggara")#CRLF

#3. Raw string Literal
#hati hati
print("C\folder, jadi berdekatan")
#caranya
print("C\\folder, sudah beres")
print(r"C\folder\bahdar")
#multiline string
print("""
    Nama:andi bahdar
    nickname: Deceng
    hobbby:mendaki gunung Es
""")
#multiline raw string
print(r"""
    Nama:andi bahdar
    nickname: Deceng\Prime 196
    hobbby:mendaki gunung Es
""")

#memdofikasi string di python
#1.menyambung string
nama_pendek="andi"
nama_panjang="andi bachdar dd"
nama_panggilan="Deceng"
nama_lengkap=nama_pendek + " " + nama_panjang+ "'" + nama_panggilan
print(nama_lengkap)
#menghitung jumlah string menggunakan 
#2.menghitung panjang string
panjang=len(nama_lengkap)
print("panjang dari string ini adalah ="+ nama_lengkap +"=" + str(panjang))
#3.operator untuk string
#mengecek apakah ada komponen char atau string di string
d="d"
status=d in nama_lengkap
print(d+"apakah d adah dalam nama lengkap saya :" + nama_lengkap +"="+str(status))
#mengecek apakah ada komponen char atau string di string
d="D"
status=d in nama_lengkap
print(d+"apakah D ada dalam nama lengkap saya :" + nama_lengkap +"="+str(status))

#mengulang string
print("lord"*12)
print(13*"lord")
#menghitung string
print("index ke 0 adalah: " + nama_lengkap[0])
print("index ke 7 adalah: " + nama_lengkap[7])
print("index ke 12 adalah: " + nama_lengkap[12])
print("index ke 0:3 adalah: " + nama_lengkap[0:4])
print("index ke 0 adalah: " + nama_lengkap[3:4])
print("index ke -1 adalah: " + nama_lengkap[-1])
print("index ke -4 adalah: " + nama_lengkap[-4])
print("index ke 0,2,4,6,8,10 adalah: " + nama_lengkap[0:10:2])

#menghitung item paling kecil
print("paling kecil :"+ min (nama_lengkap))
#menghitung item paling besar
print("paling besar :"+ max (nama_lengkap))
#4.operator dalam bentuk method
data="andi bachdar dd"
jumlah=nama_lengkap.count("a")
print("jumlah angka a di nama lengkap saya adalah:" + data+ "="+str(jumlah))

#operator dalam bentuk methods
## merubah semua case dari string
#merubah semua string menjadi Upper case
nama="andi bachdar dd"
nama_besar=nama.upper()
print("mengubah nama saya menjadi upper: "+nama_besar)
#merubah semua string menjadi lower case
nama_besar=nama.lower()
print("mengubah nama saya menjadi lower: "+nama_besar)
#pengecekan dengan isX method
#contoh pengecekan lower case
nama="andi"
apakah_lower=nama.islower()
print(nama+"apakah di namaku ada lowernyaa: "+str(apakah_lower))
#pnegacekan Upper
nama="Andi"
apakah_upper=nama.isupper()
print(nama+"apakah di namaku ada uppernyaa: "+str(apakah_upper))
#isalpha() ---------> untuk pengecekan semua huruf
#isalnum() ---------> untuk pengecekan semua numerik atau angka
#isdecimal() ---------> untuk pengecekan semua bilangan
#isspace() ---------> untuk pengecekan semua space di dalam string
#istitle() ---------> untuk pengecekan semua judul dalam string

judul="14 peaks nothing imposible"
cek_judul=judul.istitle()
print(judul+"apakah judul ini ada: "+str(cek_judul))
#pengecekan stratswith, endswith
name="Andi Bachdar"
cek_start=name.startswith("Andi")
print(name+"apakah ini ada?"+str(cek_start))
#pengecekan endswith
name="Andi Bachdar"
cek_start=name.endswith("bachdar")
print(name+"apakah ini ada?"+str(cek_start))
#penggabunagn komponen join(),split()
pisah=["indonesia","merdeka","1945"]
gabungan=",".join(pisah)
print(pisah)
print(gabungan)

gabungan=" ".join(pisah)
print(gabungan)
#penggabungan komponen menggunakan split
gabungan="decengselalubelajarlebihbaik"
print(gabungan.split('selalu'))
#alokasi karakter rjust(), ljust(), center()
kanan="kanan".rjust(10)
print("'"+kanan+"'")
kiri="kiri".ljust(10)
print("'"+kiri+"'")
tengah="tengah".center(20,":")
print("'"+tengah+"'")
tengah=tengah.strip(":")
print("'"+tengah+"'")

#format string
#contoh generic
#string
nama="andi"
format_string=f"halooo = {nama}"
print(format_string)
#boolean
apakah_benar=True
format_boolean=f"boolean = {apakah_benar}"
print(format_boolean)
#bilangan bulat
bilangan_bulat=26
format_bilangan_bulat=f"bilangan bulat={bilangan_bulat}"
print(format_bilangan_bulat)
#angka 
angka=250.9
format_desimal=f"bilangan desimal= {angka}"
print(format_desimal)
#bilangan ordo ribuan
angka=20000000
format_ribuan=f"bilangan ribuan={angka:,}"
print(format_ribuan)
#bilangan desimal
angka=2005.54365
format_ribuan=f"bilangan ribuan={angka:.3f}"
print(format_ribuan)
#menampilkan landing zero
angka=2005.5433365
format_ribuan=f"bilangan ribuan={angka:010.3f}"
print(format_ribuan)
#menampilkan tanda + atau -
mines=-10
plus=10.263
format_mines=f"mines={mines:+d}"
format_plus=f"plus={plus:+.2f}"
print(format_mines)
print(format_plus)
#memformat person
presentase=0.045
format_persen=f"presentase ={presentase:.2%}"
print(format_persen)
#melakukan operasi aritmatika
harga=50000
jumlah=5
pesanan=f"harga di kali jumlah{harga*jumlah}"
print(pesanan)
#melakukan operator lainya (binary,octal,hexadecimal)
angka=500
binary=f"format binary={bin(angka)}"
octal=f"format octal={oct(angka)}"
hexade=f"format hexadesimal={hex(angka)}"
print(binary)
print(octal)
print(hexade)

#with and multiline
#Data
data_nama="andi bachdar dd"
data_umur=23
data_sepatu=43.5
data_warna="Merah"

 #data string standard
data_string=f"nama={data_nama}, umur={data_umur}, nomer sepatu={data_sepatu}, warna favorite={data_warna}"
print(5*"="+"Data String"+5*"=")
print(data_string)

  #data string standard
data_string=f"\nnama={data_nama}, \numur={data_umur}, \nnomer sepatu={data_sepatu}, \nwarna favorite={data_warna}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

#data dengan modifikasi triple qoute
data_string=f"""
nama            :{data_nama}
umur            :{data_umur:>15}
nomer sepatu    :{data_sepatu:>15}
warna favorite  :{data_warna:>15}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

#membuat projek penghitung hari dan tahun lahir
import datetime as dt
print("Silahkan masukkkan tanggal, \nbulan dan tahun lahir anda\n")
tanggal=int(input("Tanggal\t:"))
bulan_lahir=int(input("Bulan\t:"))
tahun_lahir=int(input("Tahun\t:"))
tanggal_lahir= dt.date(tahun_lahir,bulan_lahir,tanggal)
print(f"Tanggal lahir anda adalah: {tanggal_lahir}")

hari_ini=dt.date.today()
print(f"hari ini tanggal\t:{hari_ini}")
umur_hari=hari_ini-tanggal_lahir
umur_tahun=umur_hari.days//365
umur_bulan_sisa=(umur_hari.days%365)//30

print(f"hari nyaa adalah hari\t:{tanggal_lahir:%A}")
print(f"Umur anda adalah\t:{umur_tahun} tahun {umur_bulan_sisa} bulan")

#if and else statement
#1.ifnya
#2.kondisinya
#3.aksinya

nama=input("Siapa nama anda: ")
#1 ifnya (inline)
#if nama=="bahdar":print("bahdar kamu keren abiezzz")
#print(f"terimkasih akhir dari program")
#2.kondisinya if identansion
#if nama=="bahdar":
#    print("kamu kece abieezz@@@@")
#    print("yang terbaik123")
#print(f"terimkasih{nama}")

if nama=="andi":
    print("kamu yang terkeren")
    print("luarbiasa berhasil")
else:
    print("kamu bukan andi")
print(f"program selesai")

#Elif = Else if statement
umur=int(input("masukkan umur anda: "))
if umur<23:
    print("kamu masih muda")
elif umur >23:
    print("kamu rentan")
elif umur >40:
    print("kamu harus waspada")
else:
    print("kamu masih muda")
print(f"umur anda adalah: {umur} tahun")

#aplikasi kolkulator
print(20*"=")
print("operator kalkulator")
print(20*"="+"\n")

angka_1=float(input("Masukkan angka 1 bang :"))
operator=input("berikut operator yang tersedia +,x,/,- :")
angka_2=float(input("Masukkan angka 2 bang : "))
#kondisinya atau elif nyaa
if operator =="+":
    hasil=angka_1+angka_2
    print(f"hasilnya adalah = {hasil}")
elif operator == "x" or operator =="*":
    hasil= angka_1 * angka_2
    print(f"hasilnya adalah = {hasil}")
elif operator =="-":
    hasil=angka_1 - angka_2
    print(f"hasilnya adalah = {hasil}")
elif operator =="/":
    hasil=angka_1 / angka_2
    print(f"hasilnya adalah = {hasil}")
else:
    print("masukkan yang ada operatornya bang")
print("program berakhir Terimaksih sudah menjalankan operatornya")

 