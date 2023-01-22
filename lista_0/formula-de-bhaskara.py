a, b, c = map(float, input().split())
delta = b ** 2 - 4 * a * c
if delta < 0 or a == 0.0:
   print("Impossivel calcular")
else:
    raio1 = (delta ** 0.5 - b) / (2 * a)
    raio2 = (-delta ** 0.5 - b) / (2 * a)
    print('R1 = ' '%.5f' % raio1)
    print('R2 = ' '%.5f' % raio2)
