class Solution(object):
    def searchRange(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        lower_bound = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                lower_bound = mid
                high = mid - 1
            else:
                low = mid + 1

        if lower_bound == -1 or nums[lower_bound] != target:
            return [-1, -1]

        low = 0
        high = n - 1
        upper_bound = n

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                upper_bound = mid
                high = mid - 1
            else:
                low = mid + 1

        return [lower_bound, upper_bound - 1]
