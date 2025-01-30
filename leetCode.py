a = int(input())
T = True
i = 1
hasil = 1
while i <= 5:
    if a%i == 0:
        hasil = hasil*i
    i+= 1
if hasil != a:
    T = False
print(T)

