class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        l = 2
        r = 2
        if n == 1:
            return 1
        while r<n:
            if nums[r]!= nums[l-2]:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
            r+=1
        return l
