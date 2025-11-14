son = int(input("nechta son kiritasan: "))
sonlar = list(map(int, input("sonlarni kiriting: ").split()))
yangi = []
for i in sonlar:
    if sonlar.count(i)!=1:
        yangi.append(i)
print(yangi)

