comp,papel,cota = map(int, input().split())
total = comp * cota
if total <= papel:
    print('S')
else:
    print('N')
