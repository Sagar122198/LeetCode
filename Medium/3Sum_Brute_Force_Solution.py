class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        my_set = set()
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k] == 0:
                        temp = [nums[i],nums[j],nums[k]]
                        temp.sort()
                        my_set.add(tuple(temp))
        return [list(ans) for ans in my_set]
