from math import *
from time import time

A = [4,7,6,2,8,3,5,1]
n = len(A)

f = open('IntegerArray.txt')
A = f.read().splitlines()
n = len(A)

for i in range(n):
	A[i] = int(A[i])

def merge1(A,l,m,r):
	B = A[:]
	i = l
	j = m+1
	k = l

	while i <= m and j <= r:
		if A[i] <= A[j]:
			B[k] = A[i]
			i+=1
		else:
			B[k] = A[j]
			j+=1
		k+=1

	if i > m:
		for h in range(j,r+1):
			B[k+h-j] = A[h]
	else:
		for h in range(i,m+1):
			B[k+h-i] = A[h]
	
	#for h in range(l,r+1):
	#	A[h] = B[h]
	A = B
	
def merge2(A,l,m,r):
	B = A[:]
	B[l:m+1] = A[l:m+1]
	B[m+1:r+1] = A[r:m:-1]
	
	p = l
	q = r
	for i in range(l,r+1):
		if B[p] <= B[q]:
			A[i] = B[p]
			p += 1
		else:
			A[i] = B[q]
			q -= 1

def merge(left, right):
	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result += left[i:]
	result += right[j:]
	return result

def mergesort(A):
	if len(A) < 2:
		return A

	m = len(A)/2
	left = mergesort(A[:m])
	right = mergesort(A[m:])
	return merge(left,right)

t = time()
mergesort(A)
print time()-t
