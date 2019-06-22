try:
    sayi_bir = int(input("lütfen birinci sayıyı girin : "))
    sayi_iki = int(input("lütfen ikinci sayıyı girin : "))

    toplam = sayi_bir + sayi_iki
    fark   = sayi_bir - sayi_iki
    bolum  = sayi_bir / sayi_iki
    carpım = sayi_bir * sayi_iki

    print( "sayıların toplamı :",toplam,
          "\nsayılatın farkı :",fark,
          "\nsayıların bölümü :",bolum,
          "\nsayıların çarpımı :",carpım )

except ValueError:
    print("Value Error")
except SyntaxError:
    print("Syntax Error")
except ZeroDivisionError:
    print("Zero Division Error")
except:
    print("hata mesajı")

