pa,cb,pb,ca = map(str, input().split())

pA = list(map(int, pa.split(':')))
cB = list(map(int, cb.split(':')))
pB = list(map(int, pb.split(':')))
cA = list(map(int, ca.split(':')))

pa = int(pA[0] * 60 + pA[1])
cb = int(cB[0] * 60 + cB[1])
pb = int(pB[0] * 60 + pB[1])
ca = int(cA[0] * 60 + cA[1])

duracao = ((cb + ca) - (pa + pb)) / 2
while duracao > 720:
    duracao -= 720
while duracao < 0:
    duracao += 720

fh = ((cb - pa) - duracao) / 60
while fh < 0:
    fh += 24
while fh > 12:
    fh -= 24
    
print(int(duracao),int(fh))
