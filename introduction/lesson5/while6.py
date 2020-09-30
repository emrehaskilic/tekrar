# kullanicinin disardan girdiği sayiların toplami yazın

import os
os.system("clear")

metin = input("Lütfen bir sayi giriniz:")

i = 0
toplam = 0

while i < len(metin):
    toplam = toplam + int(metin[i])
    i += 1
print("Girilen sayilarin toplamı: {}".format(toplam))    