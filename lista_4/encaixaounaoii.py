test = int(input())
for t in range(test):
    A,B = map(str, input().split())
    A = A[-len(B):]
    if int(A) == int(B):
        print('encaixa')
    else:
        print('nao encaixa')
