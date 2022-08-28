P = int(input())
while P != 0:
    pont1 = 0
    pont2 = 0
    for i in range(P):
        jog1,jog2 = map(int, input().split())
        if jog1 > jog2:
            pont1 += 1
        elif jog1 < jog2:
            pont2 += 1
    print(pont1, pont2)
    P = int(input())
