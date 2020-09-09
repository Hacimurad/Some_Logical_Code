#Elave 7 bolunen tapma
while True:
    n=int(input("Baslangic:"))
    m=int(input("Son:"))
    if n>=m:
        print("Baslangic boyuk olmalidi")
    else:
        break

toplam=0
for i in range(n,m):
    if i%7==0:
        toplam+=i
print("7 ye bolunenler:",toplam)
