#Disardan girilen bir sayinin teklik çiftlik durumunu sorgulayan bir algoritma yazınız
# ve teklik ciftlik durumunu belirtiniz
try:
    sayi = float(input("Lutfen bir sayi giriniz:"))

    mod = (sayi % 2)

    if mod == 0:
        rint("Sayi çifttir")
    else:
        print("Sayi tektir")
except Exception as mahmud:
    print("Sistem hatasi:YALNIZCA SAYI GİRİNİZ")

 