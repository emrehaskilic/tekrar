# parametre alan metdolar
#aldığı parametreye göre işlem seyrini değiştiren yapılardır,
#Kural 1) kesinlikle metod içerisinde parametrenin nereden geleceği tanımlanmaz
#Kuran 2) kesinlikle metod içerisinde parametreye değer atanmaz

#Dışardan alınan 2 sayıyı ekrana yazdıran Metod

def Hesapla(sayi1,sayi2):
    toplam = sayi1 + sayi2
    print(toplam)
Hesapla(20,30)    

s1 = int(input("Lütfen bir sayi giriniz:"))
s2= int(input("Lütfen 2. sayiyi giriniz"))

Hesapla(s1,s2)