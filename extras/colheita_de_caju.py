TIMELIMIT

L, C, M, N = map(int, input().split())
plantacao = []

for l in range(L):
	linha = list(map(int, input().split()))
	plantacao.append(linha)

qtdCajus = []
for l in range(L - M + 1):
	for c in range(C - N + 1):
		cajus = 0
		for m in range(M):
			cajus += sum(plantacao[l+m][c+N])
		qtdCajus.append(cajus)
		
print(max(qtdCajus))
	
 
