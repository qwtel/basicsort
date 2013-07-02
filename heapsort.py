from math import *
from time import time

A = [4,7,6,2,8,3,5,1]
A = [13,9,10,8,5,12,2]
n = len(A)

#f = open('IntegerArray.txt')
#A = f.read().splitlines()
#n = len(A)
#for i in range(n):
#	A[i] = int(A[i])

def swap(A,i,j):
	s = A[i]
	A[i] = A[j]
	A[j] = s

def shift_down(A,i,m):
	while 2*i <= m:
		# A[i] hat linken Nachfolger
		j = 2*i # A[j] ist linker Nachfolger
		if j < m:
			# A[i] hat rechten Nachfolger
			if A[j-1] < A[j]:
				j+=1 # A[j] ist groesster Nachfolger

		if A[i-1] < A[j-1]:
			swap(A,i-1,j-1)
			i=j # Versickere weiter
		else:
			break

def heapify(A):
	for i in range(n/2,0,-1):
		shift_down(A,i,n)

#t = time()
print A
heapify(A)
print A
for i in range(n,1,-1):
	swap(A,0,i-1)
	shift_down(A,1,i-1)
	print A
print A

#print time()-t

#s = 0
#j = int(ceil(log(n+1,2)))
#for k in range(1,j-1):
#	s += 2**(k-1)*(j-k)
#
#print s

