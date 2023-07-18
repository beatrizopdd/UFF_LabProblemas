N, M = map(int, input().split())
En, Em = map(int, input().split())
Sn, Sm = map(int, input().split())

# Criando o mapa para rastrear o caminho
mapa = [] 
for i in range(N):
    linha = [0] * M
    mapa.append(linha)

maiorCaminho = 0

  
def rastreio(mapa, l, c, celulasAndadas):

    global maiorCaminho
    global N
    global M
    global Sn
    global Sm

    # Ocupando a posição
    mapa[l][c] = 1 
    celulasAndadas += 1

    # Se chegou na saída e fez o maior caminho
    if (l == (Sn-1) and c == (Sm-1) and celulasAndadas > maiorCaminho):
        maiorCaminho = celulasAndadas

    else:
        # Direções possíveis para se andar no mapa (0,1) - direita, (0,-1) - esquerda, (1,0) - cima, (-1,0) - baixo
        # Se célula estiver disponível, avança nesse caminho
        # Caso contrário ele avança para a próxima direção
        navegacao = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for nav in navegacao:
            
            novol = l + nav[0]
            novoc = c + nav[1]
            
            comArmario = (novol % 2 != 0) and (novoc % 2 == 0) # Os armários estão nas células impares pois o mapa começa no 0
            limiteVertical = (0 <= novol <= N - 1) # True = dentro do mapa
            limiteHorizontal = (0 <= novoc <= M - 1) # True = dentro do mapa
            
            if ((comArmario == False) and limiteVertical and limiteHorizontal and (mapa[novol][novoc] == 0)):
                rastreio(mapa, novol, novoc, celulasAndadas)

    # Quando sai da condicional é porque 1- Todas as direções estão indisponíveis e 2- Não chegou no final
    # Desocupo a casa e tiro uma célula andada
    mapa[l][c] = 0 
    celulasAndadas -= 1

rastreio(mapa, (En-1), (Em-1), 0)

print(maiorCaminho)

