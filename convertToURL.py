def check(s):
	l = list()
	l = s.split()
	special = dict()
	for item in l:
		count = 0
		x = list(item)
		for i in x:
			if ord(i) > 43 and ord(i) < 47:
				count+=1
				special.update({ item : count})
			else:
				special.update({ item : 0})	
	print special				
	for item in l:
			if  special[item]== 0:
				print "http://" + item + ".com"
			else:
				print "http://" + item[:-special[item]] + ".com" + 	item[-special[item]:]
s = raw_input()
check(s)