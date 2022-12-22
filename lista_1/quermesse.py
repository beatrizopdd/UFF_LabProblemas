N = int(input())
t = 1
while N != 0:
    entrada = list(map(int, input().split()))
    for j in range(N):
        numero = entrada[j] / (j + 1)
        if numero == 1:
            print('Teste', t)
            print(j+1)
            print()
    N = int(input())
    t += 1
