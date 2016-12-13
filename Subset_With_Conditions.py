from itertools import combinations
def check(n,k,x,t):
    final = []
    for item in combinations(t, r = k):
        if max(item)-min(item)<=x:
            final.append(item)
    print len(final)%10000000007
    
n1 = int(raw_input())
for i in range(0,n1):
    e = [int(x) for x in raw_input().split()]
    n=e[0]
    k=e[1]
    X=e[2]
    t = [int(x) for x in raw_input().split()]
    check(n,k,X,t)