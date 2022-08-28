nota = int(input())
if nota <= 85:
    if nota <= 60:
        if nota <= 35:
            if nota == 0:
                print('E')
            else:
                print('D')
        else:
            print('C')
    else:
        print('B')
else:
    print('A')
