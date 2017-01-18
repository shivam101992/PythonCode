def check(t):
    j = 0
    i = 0
    while i < len(t):
        if t[i] != 0:
            t[j] = t[i]
            j += 1
        i+=1
    while j < len(t):
        t[j] = 0
        j += 1
    print ' '.join(str(x) for x in t)        
n = int(raw_input())
for i in range(0,n):
    n = raw_input()
    t = [int(x) for x in raw_input().split()]
    check(t)