# HATA MESAJI


try:
    sayi = int(input("sadece sayısal veri gitin : "))
    print("gelen sayı", sayi)
    #sayi = sayi / 0
    sayi = str(sayi) / 0
    print("işlem sonu")

except ValueError as ex:
    print("Value Error")
    print("sistem hata mesajı",ex)
except ZeroDivisionError as ex:
    print("Zero Division Error")
    print("sistam hata mesajı",ex)
except Exception as ex:
    print("except")
    print("sistam hata mesajı", ex)

