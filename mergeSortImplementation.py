def mergeSort(t):
	if len(t) == 1:
		return t
	else:
		l1, l2 = [],[]
		l1 = t[:len(t)//2]
		l2 = t[len(t)//2:]

		mergeSort(l1)
		mergeSort(l2)

		i,j,k = 0,0,0
		while i < len(l1) and j < len(l2):
			if l1[i] < l2[j]:
				t[k] = l1[i]
				i += 1
			else:
				t[k] = l2[j]
				j += 1
			k += 1	
		while i < len(l1):
			t[k] = l1[i]
			i += 1
			k += 1
		while j < len(l2):
			t[k] = l2[j]
			j += 1
			k += 1
		return t
						 
if __name__=="__main__":
	t = [int(x) for x in raw_input().split()]
	print mergeSort(t)		