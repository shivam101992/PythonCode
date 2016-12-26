def binary_search(t,item):
	first = 0
	last = len(t)-1
	isItemExists = False
	while first <= last and not isItemExists:
		mid = (first + last) // 2
		if item == t[mid]:
			isItemExists = True
			break
		elif item > t[mid]:
			first = mid + 1
		else:
			last = mid - 1
	return int(isItemExists)

if __name__=="__main__":
	t = [int(x) for x in raw_input().split()]
	item = raw_input()
	print binary_search(t,int(item))	