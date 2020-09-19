data =[]
n=int(input("Ne qeder eded girmek isdeyirsen:"))
for i in range(n):
    data.append(int(input("Ededi daxil edin:")))
print(data)
toplam=0
for i in data:
    toplam+=i
print("TOplamlari:",toplam)
print("Ortalamalari:",toplam/n)