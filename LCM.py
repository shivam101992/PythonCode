#python2

a,b = [int(x) for x in raw_input().split()]
def gcd(a,b):
	if b==0:
		return a

	if b!=0:
		aprime=a%b
		return gcd(b,aprime)						

print (a*b/gcd(a,b))