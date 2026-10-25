class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        result =[]
        for i in range(0,n):
            if nums[i] != val:
                result.append(nums[i])
        nums[:] = result
