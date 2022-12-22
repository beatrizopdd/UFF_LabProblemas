a,b,c,d,e = map(int, input().split())
if a < b and b < c and c < d and d < e:
    print ('C')
elif a > b and b > c and c > d and d > e:
    print ('D')
else:
    print ('N')
