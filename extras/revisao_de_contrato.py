erro,valor = map(str, input().split())

while erro != '0' and valor != '0':
    numlista = []
    for a in valor:
        numlista.append(a)

    while erro in numlista:
        numlista.remove(erro)

    imprimir = '0'
    for b in numlista:
        imprimir += b

    print(int(imprimir))

    erro,valor = map(str, input().split())
