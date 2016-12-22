def dict_reversal(d):
	new_dict = dict()
	for k,v in d.items():
		new_dict[v] = k
	print new_dict	
x = {'1':'A', '2':'B', '3':'C'}
dict_reversal(x)
