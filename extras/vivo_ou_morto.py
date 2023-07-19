participantes, rodadas = map(int, input().split())
t = 1
while participantes or rodadas != 0:
      fila_inicial = list(map(int, input().split()))
      for i in range(rodadas):
            acontecido = list(map(int, input().split()))
            gabarito = acontecido[2:]
            while 0 in fila_inicial:
                  fila_inicial.remove(0)
            for j in range(acontecido[0]):
                  if gabarito[j] != acontecido[1]:
                        fila_inicial[j] = 0           
      vencedor = max(fila_inicial)
      print('Teste', t)
      print(vencedor)
      print()
      t = t + 1
      participantes, rodadas = map(int, input().split())
