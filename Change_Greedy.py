# Uses python2

def get_change(n):
	tens=0
	fives=0
	ones=0
	if n>=10:
		tens=int(n/10)
		n=n-(tens*10)
	if n>=5:
		fives=int(n/5)
		n=n-(fives*5)
	ones=n
	return tens+fives+ones

if __name__ == '__main__':
    n = int(input())
    print(get_change(n))
