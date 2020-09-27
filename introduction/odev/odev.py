
print("""


*******************************
*                             *
*******TELEFON REHBERİ*********  
*                             *
*******************************
!KAYIT EKLEMEK İÇİN 1'i
!KAYIT DÜZENLEMEK İÇİN 2'yi
!KAYIT SİLMEK İÇİN 3'ü
!KAYIT LİSTESİ İÇİN 4'ü
!REHBERDE ARAMA YAPMAK İÇİN 5'i
-------- tuşlayınız---------

""")



deger = input("Lütfen Yapmak İstediginiz islemi Seciniz:")

rehber = [
    {
        "id"   : "0" ,
        "isim" : "Emre" ,
        "soyisim": "Haskılıç" ,
        "mail": "emre.haskilic@gmail.com" ,
        "telefon" : "+905059796816",

    }

         ]




isim = input("İsim:")
soyisim = input("Soyisim:")
mail = input("Mail:")
telefon = input("Telefon No:")
id =len(rehber)


if deger == 1:
    

    rehber.append(
{ 
    "id":id,
    "isim":isim,
    "soyisim":soyisim,
    "mail":mail,
    "telefon":telefon
}
              )
    print("Kayıt Başarıyla eklendi")

yn = input("Yeni Bir İşlem İstiyor musunuz?:(Y/N)")

if yn == "N":
    print("Güle Güle")





  

