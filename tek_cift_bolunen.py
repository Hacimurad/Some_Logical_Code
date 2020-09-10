#9 dene tek ve cutu ededi  tap topla
tek_eded=0
tek_toplam=0
cift_eded=0
cift_toplam=0
for i in range(1,10):
    s=int(input(f"{i}-ci ededi daxil edin"))
    if s%2==1:
        tek_eded+=1
        tek_toplam+=s
    else:
        cift_eded += 1
        cift_toplam += s


print(tek_eded," tek ededi var.","Toplami:",tek_toplam)
print(cift_eded,"Cut ededi var.","Toplami:",cift_toplam)