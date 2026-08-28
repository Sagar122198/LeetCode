class Solution(object):
    def removeDuplicates(self, nums):
        ### didn't work with -1 values, can't find the solution.
        # n = len(nums)
        # fm = {}
        # for i in range(0,n):
        #     fm[nums[i]] = 0

        # j = 0
        # for k in fm:
        #     nums[j] = k
        #     j +=1
        # return j

        n = len(nums)
        i = 0
        j = i+1
        if n == 1:
            return 1
        else:
            while j<n:
                if nums[i]!=nums[j]:
                    i+=1
                    nums[i],nums[j] = nums[j],nums[i]
                j+=1
            return i+1

            
        
