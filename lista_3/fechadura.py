pinos,meta = map(int, input().split())
alturas = list(map(int, input().split()))

movi = 0

while alturas != []:
      
      dif = meta - alturas[0]
      
      alturas[0] = alturas[0] + dif
      alturas[1] = alturas[1] + dif

      if alturas[1] == meta:
            alturas.pop(1)
      alturas.pop(0)

      if dif < 0:
            dif *= -1
      movi += dif
print(movi)
