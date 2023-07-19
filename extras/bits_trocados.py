dinheiro = 1
t = 1
dinheiro = int(input())

while dinheiro != 0:
    
    cinquenta = 0
    dez = 0
    cinco = 0
    um = 0
    
    manipular = dinheiro

    while manipular != 0:
        
        if manipular >= 50:
            manipular -= 50
            cinquenta += 1

        elif manipular >= 10:
            manipular -= 10
            dez += 1

        elif manipular >= 5:
            manipular -= 5
            cinco += 1
            
        elif manipular >= 1:
            manipular -= 1
            um += 1
    
    print('Teste', t)
    print(cinquenta,dez,cinco,um)
    print()
    t += 1
    
    dinheiro = int(input())
