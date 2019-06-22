# programcı hataları (error)
# program kusurları  (bug)
# istisnalar         (exception)
# mantıksal hatalar
print("sad")


try:
    telefon_numarasi = input("lütfen telefon numaranızı giriniz : ")
# telefon numarası veri tabanına kaydedildi
    print("telefon numaranız :",int(telefon_numarasi))
except ValueError:
    print("işlem hatası")
    print("lütfen geçerli bir sayı girin")
except ZeroDivisionError:
    print("işlem hatası")
    print("sıfıra bölünme hatası")

