A = ['x',4,8,6,1,7,3,5,2,9]
n = len(A)

def swap(A,i,j):
	s = A[i]
	A[i] = A[j]
	A[j] = s

def min_index(A,l,r):
	value = max(A)
	index = 0
	while l <= r:
		if A[l] < value:
			value = A[l]
			index = l
		l+=1
	
	return index

def max_index(A,l,r):
	value = min(A)
	index = 0
	while l <= r:
		if A[l] > value:
			value = A[l]
			index = l
		l+=1

	return index

def sort(A,l,r):
	if r-l > 1:
		mi = min_index(A,l,r)
		ma = max_index(A,l,r)
		swap(A,l,mi)
		swap(A,r,ma)
		sort(A,l+1,r-1)
	else:
		if r-l == 1:
			if A[l] > A[r]:
				swap(A,l,r)

sort(A,1,n-1)
print A
