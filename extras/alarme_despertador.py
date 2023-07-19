h1, m1, h2, m2 = map(int, input().split())

mDia = (24 * 60)

while (h1+m1+h2+m2 != 0):
	
	mTotal = 0 
	mAtual = (h1 * 60) + m1
	mFuturo = (h2 * 60) + m2
	
	if (mAtual > mFuturo):
		mTotal = (mDia - mAtual) + mFuturo
	
	else:
		mTotal = mFuturo - mAtual
		
	print(mTotal)

	h1, m1, h2, m2 = map(int, input().split())
	
