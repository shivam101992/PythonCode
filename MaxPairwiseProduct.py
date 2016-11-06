# Uses python2
from random import randint
#n = int(input())
#a = [int(x) for x in raw_input().split()]

#assert(len(a) == n)
def productFast(a):
	result = 0
	maxindex1=-1
	maxindex2=-1
	for i in range(0, n):
	    if (a[i]>a[maxindex1] or maxindex1 == -1):
	    	maxindex1=i

	for j in range(0, n):
	    if ((j != maxindex1) and (a[j]>a[maxindex2] or maxindex2 == -1)):
	    	maxindex2=j
   	
	result = a[maxindex1]*a[maxindex2]
	return result

def product(numbers):
	result = 0
  	n = len(numbers)
  	for i in range(0,n):
  		for j in range(i+1,n):
  			if (numbers[i] * numbers[j]) > result:
  				result = numbers[i] * numbers[j]
  	return result;

while (True):
	a=list()
	n=randint(2,100)
	for i in range(0,n):
		a.append(randint(0,100000))
	for i in a:
		print i,

	res1 = product(a)
	res2 = productFast(a)

	if(res1 != res2):
		print "Wrong answer - " + str(res1) + " : " + str(res2)
		break
	else:
		print "OK!"	

