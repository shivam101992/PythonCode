def insertionSort(t):
	for i in range(1,len(t)):
		currentValue = t[i]
		j = i
		while t[j-1] > currentValue and j > 0:
			t[j] = t[j-1]
			j = j - 1
		t[j] = currentValue	
	for item in t:
		print item,

if __name__=="__main__":
	t = [int(x) for x in raw_input().split()]
	insertionSort(t)
