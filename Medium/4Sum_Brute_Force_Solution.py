class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums)
        result = set()
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for l in range(k+1,n):
                        if nums[i]+nums[j]+nums[k]+nums[l] == target:
                            temp = [nums[i],nums[j],nums[k],nums[l]]
                            temp.sort()
                            result.add(tuple(temp))
        return [list(ans) for ans in result]
