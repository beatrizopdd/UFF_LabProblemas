tenta = int(input())
quebrados = 0
for i in range(tenta):
    L,C = map(int, input().split())
    if L <= C:
        quebrados += 0
    else:
        quebrados += C
print(quebrados)
