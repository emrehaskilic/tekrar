# kullanicilarin panel üzerine girdiği metni altalta yazdırınız
import os
os.system("clear")

metin = input("Lütfen bir metin giriniz:")
i = 0
while i < len(metin):
    print(metin[i])
    i += 1
