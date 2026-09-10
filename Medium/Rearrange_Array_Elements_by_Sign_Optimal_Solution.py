class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        positive_index= 0
        negative_index = 1
        result = [0]*n
        for i in range(0,n):
            if nums[i]>0:
                result[positive_index] = nums[i]
                positive_index+=2
            else:
                result[negative_index] = nums[i]
                negative_index+=2
        return result
