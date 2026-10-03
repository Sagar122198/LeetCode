class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        for i in range(0,n):
            if nums[i] == target:
                return True
        return False
        
