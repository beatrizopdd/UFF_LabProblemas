numero_raios = int(input())

mapa = []
altura = 500
largura = 500
dois_raios = False
for uwu in range(altura+1):
    linha = []
    for owo in range(largura+1):
        linha.append(0)
    mapa.append(linha)
	
for qwq in range(numero_raios):

    cord_raio = list(map(int, input().split()))

    mapa[cord_raio[0]][cord_raio[1]] += 1
    if mapa[cord_raio[0]][cord_raio[1]] > 1:
        dois_raios = True
        print('1')
        break
		

if dois_raios == False:
    print('0')
