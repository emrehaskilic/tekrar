from random import randint
import os
os.system("clear")

# sayısal loto benzersiz, 6 adet sayı 8 kolon

counter = int(input("Lütfen kolon adedi giriniz:"))
i = 0
sayilar = []
kolonlar = []
while i < 8:
    while i < 6:
        sayi = str(randint(1,49))
        if sayi in sayilar:
            continue
        else:
            sayilar.append(sayi)
        i +=1
    kolonlar.append(sayilar)
    sayilar.sort()
    kolonlar.sort()
    print(kolonlar)
    i += 1
    

   
