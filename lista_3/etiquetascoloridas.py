equi = [0,0,0,0,0,0,0,0,0,0,'a','b','c','d','e','f']

Rh = str(input())
R = []
Gh = str(input())
G = []
Bh = str(input())
B = []

for erre in range(len(Rh)):
      R.append(str(Rh[erre]))
R.reverse()
verm= 0
for i in range(len(R)):
      if R[i] == 'a' or R[i] ==  'b' or R[i] == 'c' or R[i] == 'd' or R[i] == 'e' or R[i] == 'f':
            R[i] = equi.index(R[i])
      verm += int(R[i]) * (16 ** i)

for ge in range(len(Gh)):
      G.append(str(Gh[ge]))
G.reverse()
verd = 0
for j in range(len(G)):
      if G[j] == 'a' or G[j] ==  'b' or G[j] == 'c' or G[j] == 'd' or G[j] == 'e' or G[j] == 'f':
            G[j] = equi.index(G[j])
      verd += int(G[j]) * (16 ** j)

for be in range(len(Bh)):
      B.append(str(Bh[be]))
B.reverse()      
azul = 0
for k in range(len(B)):
      if B[k] == 'a' or B[k] ==  'b' or B[k] == 'c' or B[k] == 'd' or B[k] == 'e' or B[k] == 'f':
            B[k] = equi.index(B[k])
      azul += int(B[k]) * (16 ** k)      


qVerm = 1
qVerd = (verm // verd) * (verm // verd)
qAzul = ((verd // azul) * (verd // azul)) * qVerd
tudo = qVerm + qVerd + qAzul

convertido = []
while tudo > 0:
      sub = tudo
      tudo = tudo // 16
      restinho = int(sub - (tudo * 16))
      convertido.append(restinho)

convertido.reverse()

hexa = str()
for z in convertido:
      if z > 9:
            hexa += str(equi[z])
      else:
            hexa += str(z)
print(hexa)
