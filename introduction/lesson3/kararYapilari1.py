# KARAR  YAPILARI
# Karsilastirma operatorleri

# == (esittir) sagdaki degerin soldaki degere esit olma durumu
# 1 == 1 => true - ıf
# 1 == 2 => false - else

# != (esit degildir) soldaki degerin sagdaki degere esit olmama durumu
# 1 != 1 => false - else
# 2 != 1 =>  true - if

# > (buyuktur)
# < (kucuktur)
# >= (buyuk esittir)
# <= (kucuk esittir)

username = input("Lutfen kullanici adinizi giriniz: ")
username = username.lower()\
    .replace("ı","i")\
    .replace("ç","c")\
    .replace("ş","s")\
    .replace("ö","o")\
    .replace("ğ","g")\
    .replace("ü","u")    #replace("","") komutu soldaki karakter ve sağdaki karakterin yerini değiştirir
print(username)

if(username == "ozguc_tigmas"):
    print("Tebrikler,giriş yaptiniz")
else:
    print("Kullanici adiniz yanlis")    