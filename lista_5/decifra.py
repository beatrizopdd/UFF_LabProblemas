normal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
chave = []
decifrado = []

cifra = input()
charada = input()


for i in cifra:
    chave.append(i)

for j in charada:
    local = chave.index(j)
    decifrado.append(normal[local])

X = str()
for k in decifrado:
    X += k
 
print(X)
