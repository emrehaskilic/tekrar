# birden fazla elemanla çalışacak sek tek tek değişken tanımlamak yerine dizi kullanıyorum
# tanımlama şekli:

sehirler = ["istanbul","edirne","konya","rize","ankara","eskisehir","adana","kayseri"]

# not: bir dizinin eleman sayisi x ise index sayisi x-1'dir

print(sehirler[-1]) # listenin son elemanını yazdırdı

index = len(sehirler)
print(index)

print(sehirler[2:7])

# 2. ve 7. degerler dahil sıralar

print(sehirler[:]) # listenin tüm elemanlarını ekrana yazdırır

#Kullanıcı dışardan sehir adı girecek 
#sehir adı listede ise : ..... sehri dizi içinde bulunmaktadır
# sehir adı listede degil ise .... sehri dizi icinde bulunmamaktadır yazdırınız

city = str(input("Lütfen şehir adı giriniz:"))

if city in sehirler:
    print(f"{city} sehri dizi içerisindedir",city)
else:
    print(f"{city} sehri dizi içerisinde degildir")  


list1 = ["sehirler dizisi"]
print(list1)

list2 = ["arabalar dizisi"]
print(list2)

list3 = ["renkler dizisi"]
print(list3)

result = list(zip(list1,list2,list3))
print(result)




