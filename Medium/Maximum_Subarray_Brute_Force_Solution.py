class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        maxi = float("-inf")
        for i in range(0,n):
            total = 0
            for j in range(i,n):
                total = total+nums[j]
                maxi = max(maxi,total)
        return maxi
