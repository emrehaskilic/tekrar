#Kullanicidısardan not girecek ve girilen not 0 dan kucukse "0 dan kucuk deger giremezsiniz"
# 100 den buyukse "100" den buyuk not giremezsiniz uyarısı
# girilen not 0 ve 100 arasinda ise (0 ve yüz dahi) girilen notu gösteriniz
try:
    puan = int(input("LÜTFEN ALINAN PUANI GİRİNİZ:"))

    if puan < 0:
     print("0'dan küçük not giremezsiniz")
    elif puan > 100:
        print("100'den büyük değer giremezsiniz")
    else:
        print("Aldığınız Puan:",puan)
except:
    print("Sadece not giriniz")            