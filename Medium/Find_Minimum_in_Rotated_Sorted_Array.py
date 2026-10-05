class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        minimum = float("inf")
        low = 0 
        high = n-1
        while low<=high:
            mid = (low + high)//2   
            if nums[mid]<=nums[high]:
                minimum = min(minimum,nums[mid])
                high = mid-1
            else:
                minimum = min(minimum,nums[mid])
                low = mid+1        
        return minimum
