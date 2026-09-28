class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums)
        result = set()
        for i in range(0,n):
            for j in range(i+1,n):
                my_set = set()
                for k in range(j+1,n):
                    l = target-(nums[i]+nums[j]+nums[k]) 
                    if l in my_set:
                        temp = [nums[i],nums[j],nums[k],l]
                        temp.sort()
                        result.add(tuple(temp))
                    my_set.add(nums[k])
        return [list(ans) for ans in result]
