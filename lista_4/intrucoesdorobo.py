testes = int(input())
for t in range(testes):
      P = 0
      comandos = [0]
      
      numcom = int(input())
      for n in range(numcom):
            com = str(input())
            if 'SAME' in com:
                  com = list(map(str, com.split()))
                  X = int(com[-1])
                  comandos.append(comandos[X])
            else:
                  comandos.append(com)

                  
      for i in comandos:
            if i == 'LEFT':
                  P -= 1
            elif i == 'RIGHT':
                  P += 1

      print(P)
