class Solution(object):
    def merge_array(self, left , right):
        result = []
        n,m = len(left),len(right)
        i,j = 0,0
        while i<n and j<m:
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        while i<n:
            result.append(left[i])
            i+=1
        while j<m:
            result.append(right[j])
            j+=1
        return result
    
    def sortColors(self, nums):
        n = len(nums)
        if n <= 1:
            return nums
        mid = n //2
        left_arr = nums[:mid]
        right_arr = nums[mid:]
        left = self.sortColors(left_arr)
        right = self.sortColors(right_arr)
        results = self.merge_array(left,right)
        nums[:] = results
        return nums
        

        
