# print(''f'')
# print(1)

# degisken tanimlama kurallari
# 1) degisken ismi sayi ile baslayamaz
# 2) degisken , iki kelimeden olusamaz (ayrik)
# 3) degisken, ismi içerisinde sadece izin verilen özel karakter kullanilabilir(_)
# 4) önemli kural: degisken, tanimlamisi yapilirken, kesinlikle tanimli kelimeler kullanilmaz
# 5) degisken, isimi içerisinde türkçe kelimeler kullanmayiniz


#  int, string, float

sayi=5 # int tam sayi veri tipi
print(sayi)
print(type(sayi))

ondalikli_sayi= 4.6
print(ondalikli_sayi)
print(type(ondalikli_sayi))

isim = "beste"
soyisim = "karademir"

print(isim)
print(soyisim)
print(isim + " "+ soyisim)
print(isim,"",soyisim)
print(isim, soyisim)


fullname = isim + " " + soyisim

print("kullanici adi :",fullname)


x = True
y = False

print(x)
print(y)

print(fullname*5)
# \n bir alt satýra geçmek
print((fullname +"\n")*5)


print(type(fullname))

######################################################################################


## convert : elinizdeki bir veri tipini baska bir veri tipine cevirmek icin kullaniriz

# int()





sayi1 = input("Lutfen bir sayi giriniz: ")
sayi2 = input("Lutfen bir sayi giriniz: ")

sonuc = int(sayi1) + int(sayi2)
print(sonuc)
print(type(sonuc))

print("islem sonucu : ", sonuc)
print(type(sonuc))

print('islem sonucu : '+ str(sonuc))

print("""
      bilge
      adam
      besiktas""")



# "bilge adam"
# 'bilge adam'
# """bilge adam"""

print("bilge adam \"besiktas\" istanbul")

 # bilge adam " besiktas" istanbul

 print("bilge adam \"besiktas\" istanbul\n\
       yazilim dersleri\
       python ogreniyoruz")

































 





















































