try:
    sayi1 = int(input("lutfen sayi giriniz: "))
    sayi2 = int(input("lutfen sayin giriniz:"))

    sonuc = sayi1 / sayi2

except ValueError as aa:
    print("islem hatasi:",aa)
else:
    try:
        print(sayi1/sayi2)
        print("islem sonucu")
    except ZeroDivisionError as aa:
        print(aa)

    
