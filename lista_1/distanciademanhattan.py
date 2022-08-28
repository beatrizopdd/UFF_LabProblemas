Xm,Ym,Xr,Yr = map(int, input().split())
xmenos = abs((+Xr) - (+Xm))
ymenos = abs((+Yr) - (+Ym))
distancia = xmenos + ymenos
print(distancia)
