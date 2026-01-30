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
