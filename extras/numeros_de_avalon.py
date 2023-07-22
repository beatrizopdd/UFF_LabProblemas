TIMELIMIT

num, mes, ano = map(int, input().split())

sequencia = []
valor = 0

while (len(sequencia) < num):
	
	valor += 1
	checaMes = str(mes) not in str(valor)
	checaAno = str(ano) not in str(valor)
	
	if (checaMes and checaAno):
		sequencia.append(valor)

print(sequencia[-1])
