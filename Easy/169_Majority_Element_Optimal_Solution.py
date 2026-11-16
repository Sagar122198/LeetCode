### Boyer-Moore Voting Algorithm ###
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0
        for i in range(0,len(nums)):
            if count == 0:
                candidate = nums[i]
                count = 1
            elif nums[i] == candidate:
                count+=1
            else:
                count-=1
        return candidate       
