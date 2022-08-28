valores = [4,5,6,7,12,11,13,1,2,3]

partidas = int(input())

pada = 0
pber = 0


for i in range(partidas):
      cartas = list(map(int, input().split()))
      rada = 0
      rber = 0
      for r in range(3):
            a = valores.index(cartas[r])
            b = valores.index(cartas[r + 3])
            if a >= b:
                  rada += 1
            else:
                  rber += 1
      if rada > rber:
            pada += 1
      else:
            pber += 1

print(pada,pber)
