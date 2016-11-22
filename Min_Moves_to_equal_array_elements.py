class Solution(object):
    def minMoves2(self, nums):
        nums = sorted(nums)
        if len(nums)%2==0:
            mid = nums[len(nums)//2]
        else:
            mid = nums[len(nums)/2]
        a = list()
        s=0
        for i in nums:
            a.append(mid - i)
        for i in a:
            s += abs(i)
        return s