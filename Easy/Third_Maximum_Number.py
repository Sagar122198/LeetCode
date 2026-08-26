class Solution(object):
    def thirdMax(self, nums):
        l = float("-inf")
        sl = float("-inf")
        tl= float("-inf")
        n = len(nums)
        for i in range(0,n):
            l = max(l , nums[i])
        for i in range(0,n):
            if nums[i]>sl and nums[i] != l:
                sl = nums[i]
        for i in range(0,n):
            if nums[i]>tl and nums[i] != sl and nums[i] !=l:
                tl = nums[i]
        if tl == float("-inf"):
            return l
        return tl
