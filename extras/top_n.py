T = 0

N = int(input())

if N == 1:
    T = 1
elif 1 < N <= 3:
    T = 3
elif 3 < N <= 5:
    T = 5
elif 5 < N <= 10:
    T = 10
elif 10 < N <= 25:
    T = 25
elif 25 < N <= 50:
    T = 50
else:
    T = 100
 
print('Top',T)
