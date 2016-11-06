#Sum of each subset

def subsets(nums):
  if nums is None: return None
  subsets = [[]] 
  next = [] 
  for n in nums:
    for s in subsets:
      next.append(s + [n])
    subsets += next
    next = []
  return subsets
  
def check(t):
    final = list()
    subset = list()
    subset = subsets(t)
    for item in subset:
        final.append(sum(item))
    print ' '.join(str(x) for x in sorted(final))
n = int(raw_input())
for i in range(0,n):
    t = int(raw_input())
    arr = [int(x) for x in raw_input().split()]
    check(arr)