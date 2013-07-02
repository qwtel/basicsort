from math import *
from time import time

A = [4,7,6,2,8,3,5,1]
f = open('IntegerArray.txt')
A = f.read().splitlines()
n = len(A)

for i in range(n):
	A[i] = int(A[i])

def merge_and_count_inv(A,l,m,r):
	B = A[:]
	B[l:m+1] = A[l:m+1]
	B[m+1:r+1] = A[r:m:-1]
	
	p = l
	q = r
	s = 0
	for i in range(l,r+1):
		if B[p] <= B[q]:
			A[i] = B[p]
			p += 1
		else:
			A[i] = B[q]
			q -= 1
			s += (m+1)-p

	return s

def sort_and_count(A,l,r):
	if not l < r:
		return 0
	else:
		m = int(floor((l+r)/2))
		x = sort_and_count(A,l,m)
		y = sort_and_count(A,m+1,r)
		z = merge_and_count_inv(A,l,m,r)
	
	return x+y+z

t = time()
print sort_and_count(A,0,n-1)
print time()-t

#print A
