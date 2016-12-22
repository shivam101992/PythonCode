import sys
def check(t):
    if t[0] == 0:
        print -1
    else:    
        jumps = list()
        actualjump = range(len(t))
        actualjump[0]=0
        jumps.append(0)
        for i in range(1,len(t)):
            jumps.append(sys.maxint)
            for j in range(0,i):
                if i <= (j+t[j]):
                    if jumps[i] > jumps[j]+1:
                        jumps[i] = jumps[j] + 1
                        actualjump[i] = j
        x = list(set(jumps))
        l = dict()
        for item in x:
            for i, j in enumerate(jumps):
                if j == item:
                    l.update({item : i})
        print l            
n = int(raw_input())
for i in range(0,n):
    t = [int(x) for x in raw_input().split()]
    check(t)