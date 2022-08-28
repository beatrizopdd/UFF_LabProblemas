risada = str(input())
vogais = ['a','e','i','o','u']
re = []
rd = []

for i in risada:
      if i in vogais:
            re.append(i)

rd = re[:]
rd.reverse()

tamanho = len(re)
confere = 0

for j in range(tamanho):
      if rd[j] == re[j]:
            confere += 1
      else:
            confere += 0

if confere == tamanho:
      print('S')
else:
      print('N')
