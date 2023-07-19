nJogadores, nRodadas = map(int, input().split())
lPontos = list(map(int, input().split()))

placar = [0] * nJogadores
maior = 0
vencedor = 0

for jogador in range(nJogadores):
    for ponto in range(jogador, (nJogadores*nRodadas), nJogadores):
            placar[jogador] += lPontos[ponto]	
            
            if (ponto >= (nJogadores * (nRodadas-1)) and placar[jogador] > maior):
            	maior = placar[jogador]
            	vencedor = jogador + 1
            	
print(vencedor)
