# kullanıcı dışarıdan şifre gidecek girilen şifre 3 ile 8 aralığında ise şifremiz
# şifreniz: şifre olarak onaylandı
# kullanıcı 3 denemenin sonunda beceremezse, motive edici bir mesaj veriniz :)


for i in range(1,3):
    password = input("Lütfen parolayı giriniz")
    if i == 2:
        print("Sifrenizi 3 defa yanlış girdiniz tekrar dene")
    elif not password:
        print("Sifreoluşturabilmek için tek tuşabas")
    elif len(password) in range(3,8):
        print(f"Sifreniz:{password} olarak belirlenmiştir") 
        break       