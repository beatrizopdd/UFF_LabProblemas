grana, jogos = map(int, input().split())
D = grana
E = grana
F = grana
for i in range(jogos):
    capitalismo = list(map(str, input().split()))
    capitalismo[-1] = int(capitalismo[-1])
    if capitalismo[0] == 'C':
        if capitalismo[1] == 'D':
            D = D - capitalismo[2]
        elif capitalismo[1] == 'E':
            E = E - capitalismo[2]  
        elif capitalismo[1] == 'F':
            F = F - capitalismo[2]
            
    elif capitalismo[0] == 'V':
        if capitalismo[1] == 'D':
            D = D + capitalismo[2]
        elif capitalismo[1] == 'E':
            E = E + capitalismo[2]
        elif capitalismo[1] == 'F':
            F = F + capitalismo[2]
            
    elif capitalismo[0] == 'A':
        if capitalismo[1] == 'D':
            if capitalismo[2] == 'E':
                D = D + capitalismo[3]
                E = E - capitalismo[3]
            elif capitalismo[2] == 'F':
                D = D + capitalismo[3]
                F = F - capitalismo[3]
        elif capitalismo[1] == 'E':
            if capitalismo[2] == 'D':
                E = E + capitalismo[3]
                D = D - capitalismo[3]
            elif capitalismo[2] == 'F':
                E = E + capitalismo[3]
                F = F - capitalismo[3]
        elif capitalismo[1] == 'F':
            if capitalismo[2] == 'D':
                F = F + capitalismo[3]
                D = D - capitalismo[3]
            elif capitalismo[2] == 'E':
                F = F + capitalismo[3]
                E = E - capitalismo[3]
                
print(D, E, F)
