#python2

n,m = [int(x) for x in raw_input().split()]
a=list()
a.append(0)
a.append(1)

def get_pisano_period(n, m):
    fib = 1
    fib_prev = 0
    i = 2
    while i < 6 * m and i < n:
        fib_prev, fib = fib, fib + fib_prev
        i += 1
        if (fib % m == 1 and fib_prev % m == 0):
            i -= 2
            break
    return i

n=n%get_pisano_period(n,m)

for i in range(2,n+1):
		a.append(a[i-1]+a[i-2])
print a[n]%m

