pilhas = int(input())
pedras = list(map(int, input().split()))
escada = []
total = 0
soma = 0
falta = 0
sobra = 0
for i in range(pilhas):
      total = total + pedras[i]
      soma += i
inicio = (total - soma) / pilhas

if (total - soma) % pilhas == 0:
      for j in range(pilhas):
            base = inicio + j
            escada.append(base)
      for k in range(pilhas):
            diferenca = pedras[k] - escada[k]
            if diferenca >= 0:
                  sobra += diferenca
            elif diferenca < 0:
                  falta -= diferenca
      falta = int(falta)
      print(falta)
else:
      print('-1')

