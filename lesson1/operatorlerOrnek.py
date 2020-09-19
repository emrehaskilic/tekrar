#1) Disaridan girilen 2 sayinin toplami ve farklarininn bolumunden kalanini bulunuz?
#2) Disaridan girilen 1 sayinin 10 eksiğinin 20 fazlasinin 2 ye bolumunu bulunuz?
#3) Disaridan girilen iki sayinin karelerinin toplami ve farklarinin toplamini bulunuz?
#4) Bir ders notu hesaplanirken vizenin %30 u finalin %70 inin ortalamasi aliniyor. Notu bulunuz?
#5) Disardan isim ve soyisim girerek isim.soyisim@hotmail.com seklinde yazdiriniz?

#1)
 
sayi1 = float(input("Lutfen 1. sayiyi giriniz: "))
sayi2 = float(input("Lutfen 2. sayiyi giriniz: "))
toplam = sayi1 + sayi2
fark = sayi1 - sayi2
mod = toplam % fark
print(mod)

#2)

sayi3 = float(input("Lutfen bir sayi giriniz: "))
cevap =  (((sayi3 - 10) + 20) / 2)
print(cevap)

#3)
sayi4 = float(input("ilk sayiyi giriniz: "))
sayi5 = float(input("ikinci sayiyi giriniz: "))

kareler_toplami = (sayi4**2) + (sayi5**2)
kareler_farki = (sayi4**2) - (sayi5**2)
cevap1 = kareler_toplami - kareler_farki
print(cevap1)

#4)

vize = float(input("vize notu :"))
final = float(input("final notu :"))

vizeort = (vize)*(30/100)
finalort = (final)*(70/100)

sonnot = (vizeort + finalort)

print(f"Ders notu:",(sonnot))


#5)
 
isim = str(input("İsim: "))
soy_isim = str(input("Soyisim: "))

mail = "{}.{}@hotmail.com".format(isim,soy_isim)
print(mail)






    