postos,dim = map(int, input().split())
posi = list(map(int, input().split()))
ok = 0

posi.append(42195)
posi.reverse()

for i in range(postos):
      dista = posi[i] - posi[i + 1]
      if dista <= dim:
         ok += 1
      else:
         ok += 0
         
if ok == postos:
      print('S')
else:
      print('N')
