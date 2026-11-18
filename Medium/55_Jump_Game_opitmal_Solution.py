class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums)==1:
            return True
        i = 0
        j = 0
        while i<len(nums):
            if i>j:
                return False 
            j = max(j, i + nums[i])
            if j >= len(nums)-1:
                return True
            i+=1
        return False 
