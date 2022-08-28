L,C = map(int, input().split())
sLin = []
sCol = [0] * C

maior = []

for i in range(L):
      linha = list(map(int, input().split()))
      for j in range(C):
            sCol[j] += linha[j]
      sLin.append(sum(linha))

maior.append(max(sLin))
maior.append(max(sCol))

print(max(maior))
