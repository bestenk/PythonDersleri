try:
    sayi_bir = int(input("bölünecek sayi girin"))
    sayi_iki = int(input("bölünecek olan sayiyi girin"))

    #sonuc = sayi_bir / sayi_iki
    #print("işlem sonucu :",sonuc)
except ValueError as ex:
    print("işlem hatası :",exp)
else:
    try:
        print(sayi_bir/sayi_iki)
    except ZeroDivisionError:
        print("sayı 0 değerine bölünemez!")

