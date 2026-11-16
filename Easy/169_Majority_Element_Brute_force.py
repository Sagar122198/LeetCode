class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        dic = {} 
        for i in range(0,n):
            if nums[i] in dic:
                dic[nums[i]] +=1
            else:
                dic[nums[i]] = 1
        largest = 0
        for v in dic.values():
            largest = max(v,largest)
        
        for key, val in dic.items():
            if val == largest:
                return key 
