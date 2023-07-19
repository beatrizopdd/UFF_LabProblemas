N = int(input())
t = 1
while N != 0:
  jog1 = input()
  jog2 = input()
  print('Teste', t)
  for i in range(N):
    A,B = map(int, input().split())
    c = A + B
    if c % 2 == 0:
      print(jog1)
    else:
      print(jog2)
  print()
  t = t + 1
  N = int(input())
