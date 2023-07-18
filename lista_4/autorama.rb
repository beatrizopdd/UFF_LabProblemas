P,C,V = map(int, input().split())
placar = [0] * C
quando = [0] * C
jadeuvolta = []

for medicao in range(V):
    carro,posto = map(int, input().split())
    if posto - placar[carro - 1] == 1:
        placar[carro - 1] = posto
        quando[carro - 1] = medicao
    if placar[carro - 1] == P:
        placar[carro - 1] = 0
        jadeuvolta.append(carro)

for bonus in jadeuvolta:
    placar[bonus - 1] += P

podio = []
while max(placar) != 0:
    cmaispontos = placar.index(max(placar))
    for w in range(cmaispontos,C):
        if placar[w] == max(placar) and quando[w] < quando[cmaispontos]:
            cmaispontos = w
    podio.append(cmaispontos + 1)
    placar[cmaispontos] = 0

imprimir = str(podio[0])
podio.pop(0)
for numero in podio:
    imprimir += ' '
    imprimir += str(numero)

print(imprimir)
