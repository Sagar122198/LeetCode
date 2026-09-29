class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        l = 0
        h = n-1
        mid = 0
        while mid<=h:
            if nums[mid] == 0:
                nums[l],nums[mid] = nums[mid], nums[l]
                l +=1
                mid +=1
            elif nums[mid] == 1:
                mid +=1    
            else:
                nums[mid],nums[h] = nums[h],nums[mid]
                h-=1
