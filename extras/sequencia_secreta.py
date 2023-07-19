total = int(input())
anterior = 0
historico = []
for i in range(total):
    davez = int(input())
    if davez != anterior:
        anterior = davez
        historico.append(davez)
        
print(len(historico))
