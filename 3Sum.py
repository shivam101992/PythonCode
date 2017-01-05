class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(0,len(nums)):
            j = i + 1
            k = len(nums)-1
            while j < k:
                s = nums[i] + nums[j]
                if s + nums[k] < 0:
                    j+=1
                elif s + nums[k] > 0:
                    k -=1
                else:
                    if [nums[i],nums[j], nums[k]] in res:
                        j += 1
                        k -= 1
                        continue
                    else:
                        res.append([nums[i],nums[j], nums[k]])
                        j += 1
                        k -= 1
        return res

if __name__=="__main__":
    print threeSum([-1,0,1,2,-1,-4])        