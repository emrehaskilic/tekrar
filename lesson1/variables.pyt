print("hello world")

#degisken tanimlama kurallari
# 1) degisken ismi sayi ile baslayamaz
# 2) degisken, 2 yada fazla kelimeden olusamaz olusacak ise ornk;
# benim_kullaniciAdim seklinde olur
# 3) degisken tanimlaması yapilirken kesinlikle tanimli kelimeler kullanilamaz
# 4) degisken adinda lutfen rica ediyorum :))) turkce kelime kullanmayınız

benim_adim = "emre haskilic"
mail_adresim = "emrehaskilic1@gmail.com"
adim = "emre"
soyadim = "haskilic"   #str yazarken " " yada ' ' kullanılabilir. onemli olan neyle basladiysak onla bitirmektir.

#int, str, float

sayi = 5 #int tam sati veri tipi ondalik deger almaz
print(sayi)

print(type(sayi)) #bununla degiskenin turu gorulebilir
print(adim)
print(soyadim)

print(adim + " " + soyadim) # emre haskilic seklinde yazar

fullname = adim + " " + soyadim
print(fullname)

# \n bir alt satira gecmek icin kullanilir => new line

print(fullname + "\n"*5)
print(type(fullname))

print("""
bilge 
adam 
yazilim
kursu
""")

print("bilge adam \"besiktas\" yazilim dersleri istanbul \n\
    python kursu\
    test satiri")


