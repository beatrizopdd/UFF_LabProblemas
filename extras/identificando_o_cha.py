tipo = int(input())
resposta = list(map(int, input().split()))
certo = 0

for i in resposta:
    if i == tipo:
        certo += 1
    
print(certo)
    
