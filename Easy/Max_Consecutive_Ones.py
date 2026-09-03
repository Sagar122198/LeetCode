class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n = len(nums)
        count = 0
        max_count = 0
        for i in range(0,n):
            if nums[i]==1:
                count+=1
            if nums[i] == 0:
                count =0
            if count>max_count:
                max_count = count
        return max_count
