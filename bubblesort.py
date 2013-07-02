A = [4,7,6,2,8,3,5,1]

A = range(9,0,-1)
n = len(A)

def swap(A,i,j):
	s = A[i]
	A[i] = A[j]
	A[j] = s

for j in range(0, n/2):
	for i in range(j, n-j-1):
	   	p = ' '
	   	for x in range(i):
	   		p += '   '
	   	p+='v  V'
	   	print p
		if A[i] > A[i+1]: swap(A,i,i+1)

	for i in range(n-j-2, j, -1):
	   	p = ' '
	   	for x in range(i-1):
	   		p += '   '
	   	p+='V  v'
	   	print p
		if A[i-1] > A[i]: swap(A,i-1,i)

print A
