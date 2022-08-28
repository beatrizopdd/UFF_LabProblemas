a,g,ra,rg = map(float, input().split())
va = ra / a
vg = rg / g
if va > vg:
    print('A')
else:
    print('G')
