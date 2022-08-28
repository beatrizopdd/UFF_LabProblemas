limite = int(input())
num1,operador,num2 = map(str, input().split())
if operador == '+':
    resultado = int(num1) + int(num2)
elif operador == '*':
    resultado = int(num1) * int(num2)
if resultado <= limite:
    print('OK')
else:
    print('OVERFLOW')
