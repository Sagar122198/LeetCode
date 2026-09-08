class Solution(object):
    def sortedSquares(self, nums):
        # Brute Force-------------->

        n = len(nums)
        l = []
        for i in range(0,n):
            l.append(nums[i]**2)
        return sorted(l)
