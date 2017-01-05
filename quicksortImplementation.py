def quickSort(t, start, end):
	if start < end:
		pivot = partition(t, start, end)
		quickSort(t, start, pivot-1)
		quickSort(t, pivot+1, end)
	return t

def partition(t, start, end):
	pivot = t[start]
	done = False
	left = start + 1
	right = end
	while not done:
		while t[left] <= pivot and left <= right:
			left += 1
		while t[right] >= pivot and right >= left:
			right -= 1		
		if right < left:
			done = True
		else:
			temp = t[right]
			t[right] = t[left]
			t[left] = temp
	temp = t[start]
	t[start] = t[right]
	t[right] = temp
	return right

if __name__=="__main__":
	t = [int(x) for x in raw_input().split()]
	s = len(t) // 2
	e = len(t)-1
	print quickSort(t,s,e)				