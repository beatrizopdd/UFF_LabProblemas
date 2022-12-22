# opcao 1 de codigo

L = int(input())
C = int(input())
if L % 2 != 0 and C % 2 != 0 or L % 2 == 0 and C % 2 == 0:
  print('1')
elif L % 2 == 0 and C % 2 != 0 or L % 2 != 0 and C % 2 == 0:
  print('0')


# opcao 2 de codigo

L = int(input())
C = int(input())
H = L + C
if H % 2 == 0:
  print('1')
elif H % 2 != 0:
  print('0')
