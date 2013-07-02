A = [4,7,6,2,8,3,5,1]
n = len(A)

def swap(A,i,j):
	s = A[i]
	A[i] = A[j]
	A[j] = s

for j in range(0,n-1):
	minpos = j
	for i in range(j+1,n):
		if A[i] < A[minpos]:
			minpos = i
	
	if minpos > j:
		swap(A, minpos, j)

print A
