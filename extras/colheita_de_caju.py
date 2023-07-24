L, C, M, N = map(int, input().split())

somaT = [0] *  (C - N + 1)
matriz = []
maior = 0

for l in range(L):
    
    linha = list(map(int, input().split()))
    
    somaC = []
    for c in range(C - N + 1):
        somaC.append(sum(linha[c:c+N]))
        somaT[c] += somaC[c]
        
        if (l >= M):
            somaT[c] -= matriz[l-M][c]
            
        if (l >= M-1 and somaT[c] > maior):
            maior = somaT[c]
            
    matriz.append(somaC)
    
print(maior)
