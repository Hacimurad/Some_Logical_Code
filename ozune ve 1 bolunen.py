#bolunen_sayi=0
for i in range(3,1000):
    bolunen_sayi=0
    for j in range(2,i):
        if(i%j==0):
            bolunen_sayi+=1
    if bolunen_sayi==0:
        print(i)