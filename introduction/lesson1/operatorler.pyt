# Aritmetik operatörler
# +,-,/,*,%,**

# sayi1 = 120
# sayi2 = 50

# toplam = sayi1 + sayi2

# print("islem sonucu"+ " "*20 + str(toplam))

#DISARDAN ALDIGINIZ HERHANGİ 2 SAYİNİN 
# TOPLAM-FARK-BOLUM-MOD-CARPİM-VE KUVVETİNİ ALINIZ

sayi1 = float(input("1. sayiyi gir: "))
sayi2 = float(input("2. sayiyi gir: "))

toplam = sayi1 + sayi2
fark = sayi1 - sayi2
bolum = sayi1 / sayi2
mod = sayi1 % sayi2
carpim = sayi1 * sayi2
kuvvet = sayi1 ** sayi2
 
sonuc= "Toplam sonucu: " + \
    str(toplam) + "\nCikarma sonucu: " + \
    str(fark)   + "\nBolme sonucu: "+ \
    str(bolum) + "\nMod sonucu: " + \
    str(mod) + "\nCarpma sonucu: " + \
    str(carpim) + "\n Kuvvet sonucu: " + \
    str(kuvvet)

print(sonuc)


