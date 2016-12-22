def check(t):
	n = len(t)
	max10 = 0
	for i in range(0,n):
		max10 = max10*10 + t[i]
	print max10	
t = [int(x) for x in raw_input().split()]
check(t)