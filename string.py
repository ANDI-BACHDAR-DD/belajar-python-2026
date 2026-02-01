
#string
data="ini adalah string"
print=(data)
print=(type(data))

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