class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        low = 0
        high = n-1
        lower_bound = n
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] >= target:
                lower_bound = mid
                high = mid-1
            else:
                low = mid+1
        return lower_bound
