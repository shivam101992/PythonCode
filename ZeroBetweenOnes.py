def check(t):
    l = []
    while t > 0:
        l.append(t%2)
        t = t//2
    l.reverse()
    count1 = 0
    for i in range(0,len(l)):
        if l[i] == 1:
            count1 += 1
    if count1 == 1: 
        print -1
        return
    max = 0
    count = 0
    i = 0
    flag1 = False
    flag2 = False
    while i < len(l):
        if l[i] == 1:
            i += 1
            count1 -= 1
            count = 0
            if flag1:
                flag2 = True
            continue 
        else:
            count += 1
            if count > max and count1 > 0:
                max = count
            flag1 = True
            i += 1
            
    if flag2:
        print max
    else:
        print 0
n = int(raw_input())
for i in range(0,n):
    t = int(raw_input())
    check(t)