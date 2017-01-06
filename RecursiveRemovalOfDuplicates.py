def check(t,s):
    a = list(t)
    if len(a) > 1:
        if a[0] == a[1]:
            k = 1
            count = 0
            while k<len(a):
                if a[0] == a[k]:
                    count += 1
                else:
                    break
                k += 1
            r = 0
            while r<=count:
                del a[0]
                r += 1
            return check(''.join(a),s)    
        else:
            s.append(a[0])
            del a[0]
            return check(''.join(a),s)
    else:
        if len(a) == 1:
            s.append(a[0])
            flag = False
            for i in range(len(s)-2):
                if s[i] == s[i+1]:
                    flag = True
                    return check(''.join(s),[])
            if not flag:
                print ''.join(s)  
        else:            
            print ''.join(s)        
n = int(raw_input())
for i in range(0,n):
    t = raw_input()
    s = []
    check(t,s)