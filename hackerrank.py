n= raw_input(' Enter -  ')
a=raw_input(' Enter - ')
b = [int(n) for n in a.split()]
if len(b)>n:
	print 'Wrong input!'
counter=0
c=list()
count=dict()
for i in range(0,len(b)):
	for j in range(i+1,len(b)):
		if (b[i]%b[j]==0 or b[j]%b[i]==0):
			count[b[i]]=count.get(b[i],0)+1

def keywithmaxval(dic):
     vals=list(dic.values())
     keys=list(dic.keys())
     return keys[vals.index(max(vals))]	 
print count
keys=count.keys()
print keys
for k in range(0,len(keys)):
	for l in range(k+1,len(keys)):
		if (keys[k]%keys[l]==0 or keys[l]%keys[k]==0):
			count[b[k]]=count.get(b[k],0)+1

print count[keywithmaxval(count)]			