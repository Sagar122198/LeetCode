class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        temp = []
        if n == 1:
            return nums
        else:
            for i in range(0,n):
                if nums[i] !=0:
                    temp.append(nums[i])
            x = len(temp)
            y = n - x
            j =0
            while j<y:
                temp.append(0)
                j+=1
            nums[:] = temp
            return nums
