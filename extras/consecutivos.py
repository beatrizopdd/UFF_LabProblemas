vezes = int(input())
num = list(map(int, input().split()))

igual = 1
ponto = []

for n in range(vezes - 1):
    davez = num[n]
    if davez == num[n + 1]:
        igual += 1
    else:
        ponto.append(igual)
        igual = 1

ponto.append(igual)
    
print(max(ponto))
