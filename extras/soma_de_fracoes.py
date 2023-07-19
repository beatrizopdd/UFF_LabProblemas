a, b, c, d = map(int, input().split())
numerador = 0
denominador = 0
if (b == d):
    denominador = b
    numerador = a + c
    
else:
    denominador = b * d
    numerador = (a * d) + (c * b)

fracao = [numerador, denominador]
for i in range(2, min(fracao) + 1):
    while (numerador % i == 0 and denominador % i == 0):
        numerador /= i
        denominador /= i

print(int(numerador), int(denominador))
