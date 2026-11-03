class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        low = 0
        high = 0
        sums = 0
        maxsum= float("-inf")
        while high <len(nums):
            sums+=nums[high]
            high+=1
            if (high-low)==k:
                maxsum=max(sums,maxsum)
                sums-= nums[low]
                low +=1
        return maxsum/k
