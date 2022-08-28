quantidade = int(input())
tamanhos = list(map(int, input().split()))

ideal = sum(tamanhos)/2
ladoA = 0
corte = 0

while ladoA != ideal:
    corte += 1
    ladoA += tamanhos[0]
    tamanhos.pop(0)
    
print(corte)
