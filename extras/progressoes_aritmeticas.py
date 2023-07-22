numeros = int(input())
lista = list(map(int, input().split()))

listaPA = []
if (numeros > 1):

    inicio = 0
    razao = lista[1] - lista[0]
    
    for fim in range(1, numeros):
        
        diferenca = lista[fim] - lista[fim-1]
        
        if (diferenca != razao):
            listaPA.append(lista[inicio:fim])
            inicio = fim
            if (fim < numeros-1):
                razao = lista[fim+1] - lista[fim]
            
    listaPA.append(lista[inicio:])
    
if (listaPA == []):
    listaPA.append(lista)
        
print(len(listaPA))
