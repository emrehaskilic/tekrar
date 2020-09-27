# Dışarıdan girilen bir kelmenin uzunlupu 8 karaktere esit ve ya uzunsa parola onaylandı kısa ise 
#daha uzun bir sifre seciniz uarisi verdiriniz

password = input("Lutfen parolanizi giriniz:")

if len(password) > 8 :
    print("Tebrikler yeni sifre oluşturdunuz")
else:
    print("Lütfen daha uzun bir sifre belirleyiniz")
        