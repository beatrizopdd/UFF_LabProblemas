div,ndiv,mul,nmul= map(int, input().split())
verificador = 0

if (div % ndiv == 0) or (div > mul) or (mul % div != 0) or (div == ndiv) or (mul == nmul):
    verificador = -1

teste = div
while verificador == 0:
    if (teste % ndiv != 0) and (nmul % teste != 0) and (mul % teste == 0):
        verificador = teste
    teste += div

print(verificador)
