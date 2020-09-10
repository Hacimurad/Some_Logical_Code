eded=int(input("Eded sayivi sec:"))
data=[]
for i in range(1,eded):
    data.append(int(input(f"{i}-eded:")))

print(data)

toplam=0
for x in data:
    toplam+=x
print("Data daxilindeki ededlerin cemi:",toplam)
print("Data ededlerinin ortalamasi:",toplam/eded)
