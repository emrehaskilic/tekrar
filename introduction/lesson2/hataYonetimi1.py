# Hatalar 4 e ayrılır
# 1) Programcı Hataları
# 2) Program Kusurları
# 3) İstisnai Hatalar
# 4) Mantiksal Hatalar

try:
    telefonNo = int(input("Lutfen telefon numaranizi girinizi: "))
    print("Tebrikler")
except ValueError:
    print("Value Error")
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("İslem Hatasi")
            
