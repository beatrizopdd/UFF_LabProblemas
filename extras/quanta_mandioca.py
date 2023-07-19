por = []
for i in range(5):
    por.append(int(input()))
    
por[0] = por[0] * 300
por[1] = por[1] * 1500
por[2] = por[2] * 600
por[3] = por[3] * 1000
por[4] = por[4] * 150

print(sum(por) + 225)
