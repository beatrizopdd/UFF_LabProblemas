x1,y1,x2,y2 = map(int, input().split())
bx1,by1,bx2,by2 = map(int, input().split())

checar = [0,0]

if (x1 <= bx1 <= x2) or (x1 <= bx2 <= x2) or (bx1 <= x1 <= bx2) or (bx1 <= x2 <= bx2):
    checar[0] = 1
if (y1 <= by1 <= y2) or (y1 <= by2 <= y2) or (by1 <= y1 <= by2) or (by1 <= y2 <= by2):
    checar[1] = 1
    
if sum(checar) == 2:
    print('1')
else:
    print('0')
