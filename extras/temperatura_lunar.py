TIMELIMIT

t = 1
medicoes, minutos = map(int, input().split())

while (medicoes + minutos != 0):

    temps = []
    medias = []
    for m in range(medicoes):
        temps.append(int(input()))
        
        if (len(temps) == minutos):
            media = int(sum(temps) / minutos)
            medias.append(media)
            temps.pop(0)
        
    menor = min(medias)
    maior = max(medias)
    
    print("Teste", t)
    print(menor, maior)
    print()
    
    t += 1
    medicoes, minutos = map(int, input().split())
