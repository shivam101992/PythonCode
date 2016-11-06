#Nth even fibonacci number

def F(x):
    List = []
    final=[]
    f = 1
    t = x*3
    List.append(f)
    List.append(f) #because the fibonacci sequence has two 1's at first
    while t>0:
        f = List[-1] + List[-2]   #says that f = the sum of the last two f's in the series
        List.append(f)
        t = t-1
    else:
        final.append(List[2::3]) 
        for item in final:
            print item[x-1]%1000000007
                
n = int(raw_input())
for i in range(0,n):
    t = int(raw_input())
    F(t)