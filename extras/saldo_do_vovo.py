dias,saldo = map(int,input().split())
dodia = []
for d in range(dias):
    saldo += int(input())
    dodia.append(saldo)
    
print(min(dodia))
