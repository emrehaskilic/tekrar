try:
    #db connection open
    sayi = int(input("sayi gir:"))
    # connection error
    print("congrats")
    #  !db connection close!
except:
    print("ı gave up") 
    #  !db connection close!
finally:
    print("her durumda tetiklenir")

#Finally'nin kullanım amacı:
# örneğin Bir fonksiyonda hata aldıktan sonra sunucuyla bağlantı kesilir
# fonksiyon basarili sonuclansada islem sonrasi sunucuyla baglanti kesilir
#finally yazıldıktan sonra ! ! ile belirtilen kodların yazımına gerek kalmaz
