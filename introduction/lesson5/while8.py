# dışarıdan girilen metin içerisinde yer alan sesli ve sessiz harfleri 
# ayrıştırınız ve kullanıcıya toplam adetlerini gösteriniz

sesliharfler = ["a","e","i","u","o"]
sesli = []
sessiz = []

metin = input("Lütfen bir metin giriniz:")
i = 0
while i < len(metin):
    karakter = metin[i]
    if i in sesliharfler:
        sesli.append(karakter)
    else:
        sessiz.append(karakter)
    i += 1
print(f"Sesli harfler:{len(sesli)}\nSessiz Harfler:{len(sessiz)}")

