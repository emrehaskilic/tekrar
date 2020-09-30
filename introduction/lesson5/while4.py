# 1 ile 1000 arasındaki tek sayılar ile çift sayıların toplam adedini ekrana yazdır

i = 0
teksayilar = 0
ciftsayilar = 0

while i < 100:
    if i % 2 == 0:
        ciftsayilar += 1
    else:
        teksayilar += 1
    i += 1
print(f"tek sayilarin adedi:{teksayilar}\nÇift sayilarin adedi:{ciftsayilar}")
