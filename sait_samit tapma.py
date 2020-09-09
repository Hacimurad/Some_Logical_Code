soz=input("Yazini elave edin:")
sait="aeiuo"
soz_saygac=0
for herf in soz:
    if herf in sait:
        soz_saygac+=1
print("Saitlerin sayi:",soz_saygac)
print("samitlerin sayi:",len(soz)-soz_saygac)
