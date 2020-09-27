#Dizi içerisinde işlem yapabilmek için o nesneye ait metodlar kullanılır

#.append() => dizi içerisine eleman eklemek için kullanırılır , ekleme işlemini dizinin sonuna ekler

sehirler = []
sehirler.append("ankara")
sehirler.append("istanbul")
sehirler.append("edirne")

print(sehirler[:])

#-----------------------------------------

# .inser() =>dizi içerisinde belirli bir alana veri eklemek için kullanılır

sehirler.insert(1,"bursa")
print(sehirler)
# insert ile hangi endekse eklemek istediğimizi seçebiliriz
#-----------------------------------------

#.pop() => dizi içerisinden eleman siler. indeks verilmezse en sondakini index verilirse verilen indexteki elemanı siler

sehirler.pop(1)
print(sehirler)

#----------------------------------------

arabalar = ["mercedes", "bmw", "range rover", "bugatti",
            "aston martin", "tofaş", "kartal", "serçe"]
#.remove remove metodu void metodtur .pop metodu gibi silinene elemanı geriye getirmez
print(arabalar)
print(arabalar.remove("tofaş"))

#----------------------------------

# .sort liste elemanlarını a dan z ye ve ya 0 dan 9 a sıralar

arabalar.sort()
print(arabalar)

del arabalar
print(arabalar) #del den sonra 
