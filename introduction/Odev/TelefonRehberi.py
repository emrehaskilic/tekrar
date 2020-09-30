print("""
*****************
*TELEFON REHBERİ*
*****************
------------------------------
- Kayıt Eklemek İçin    : 1 - 
- Kayıt Güncellemek İçin: 2 - 
- Kayıt Listelemek için : 3 -
- Kayıt Aramak için     : 4 -
- Kayıt Silmek için     : 5 -
------------------------------
Tuşlayınız...
""")

rehber = [
             {
                "Id":0,
                "İsim":"Emre",
                "Soyisim" :"Hask",
                "Telefon" :"23432",
                "Mail" : "mail"
            }
              
        
]

i = 1
while i == 1:
    soru = input("Lütfen yapmak istediğiniz işlemi seçiniz:")

    if soru == "1":
        id = len(rehber)  
            
        isim = input("İsim:")
        soyisim = input("Soyisim:")
        telefon = input("Telefon:")
        mail = input("Mail:")
         
        rehber.append(
                    {
                        "Id":id,
                        "İsim" :isim ,
                        "Soyisim" :soyisim,
                        "Telefon": telefon,
                        "Mail": mail

                    }
            )

        evethayir = str(input("kayıt başarıyla eklendi.✓ \n Devam etmek istiyor musunuz?:(E/H)"))
        if evethayir.upper() == "H":
            print("""
            *************
            * Güle Güle *
            *************
                """) 
            break 

    elif soru == "3":
        for a in rehber:
            print(a)
        evethayir = str(input("Devam etmek istiyor musunuz?:(E/H)"))
        if evethayir.upper() == "H":
            print("""
            *************
            * Güle Güle *
            *************
                """)  
            break
    elif soru == "5":
        print(rehber)
        index = int(input("Lütfen Silmek İstediğiniz İd'yi seçiniz:"))
        rehber.pop(index)
        print("Kayıt Basarıyla Silindi ✓")
        evethayir = str(input("\n Devam etmek istiyor musunuz?:(E/H)"))
        if evethayir.upper() == "H":
            print("""
            *************
            * Güle Güle *
            *************
                """)  
            break
    elif soru == "2":
        print(rehber)
        index = int(input("Lütfen Güncellemek İstediğiniz İd'yi seçiniz:"))
        rehber.update(
                    {
                        "Id":id,
                        "İsim" :isim ,
                        "Soyisim" :soyisim,
                        "Telefon": telefon,
                        "Mail": mail

                    }
                    )
        index = int(input("Lütfen Silmek İstediğiniz İd'yi seçiniz:"))
        if evethayir.upper() == "H":
            print("""
            *************
            * Güle Güle *
            *************
                """)   
            break
    # elif soru == "4":
    #     isim = input("İsim:")
    #     soyisim = input("Soyisim:")
    #     aramalistesi = [{}]
    #     aramakayıt = aramalistesi(isim,soyisim)
    #     print(f"{rehber.get(aramakayıt)}") #?????ARAMA KISMI???

 

            



