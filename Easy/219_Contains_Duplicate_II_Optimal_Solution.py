class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dic = {}
        for i in range(0,len(nums)):
            if nums[i] in dic and i - dic[nums[i]] <=k:
                return True
            dic[nums[i]] =i
        return False
