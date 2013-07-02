from math import *
from time import time

A = [4,7,6,2,8,3,5,1]
A = [5,18,33,4,55,2,1,73,19,34]
n = len(A)

#f = open('IntegerArray.txt')
#A = f.read().splitlines()
#n = len(A)

for i in range(n):
	A[i] = int(A[i])

def swap(A,i,j):
	s = A[i]
	A[i] = A[j]
	A[j] = s

def quicksort(A,l,r):
	if l < (r-1):
		x = r-1
		p = partition_vo(A,l,r,x)
		quicksort(A,l,p)
		quicksort(A,p+1,r)

def partition_vo(A,l,r,x):
	print l,r-1,A
	pivot = A[x]
	swap(A,x,r-1) # Move pivot element to end
	i = l-1
	j = r-1
	while True:
		while True:
			i+=1
			if A[i] <= pivot: break

		while True:
			j-=1
			if j <= i or A[j] >= pivot: break

		if i < j:
			swap(A,i,j)
		else: break

	swap(A,i,r-1) # Move pivot to its final place 
	return i

#t = time()
quicksort(A,0,n)
#print time()-t
print A
