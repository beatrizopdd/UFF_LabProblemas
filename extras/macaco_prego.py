teste = 1
regioes = int(input())

while (regioes != 0):

    # xE, yS----------xD, yS
    # |                   |
    # xE, yI----------xD, yI
    xE = -10001
    xD = 10001
    
    yS = 10001
    yI = -10001
    
    for retangulo in range(regioes):
        coord = list(map(int, input().split()))
        
        if (coord[2] < xD):
            xD = coord[2]
        if (coord[0] > xE):
            xE = coord[0]
        
        if (coord[1] < yS):
            yS = coord[1]
        if (coord[3] > yI):
            yI = coord[3]
        
    print("Teste", teste)
    
    if (xE < xD and yI < yS):
        print(xE, yS, xD, yI)
    else:
        print("nenhum")
    
    print()
    
    teste += 1
    regioes = int(input())
