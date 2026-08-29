class Solution(object):
    # Part of better solution
    # def reverse(self, nums , left,right):
    #     while left<right:
    #         nums[left],nums[right] = nums[right] , nums[left]
    #         left+=1
    #         right-=1
        
    def rotate(self, nums, k):
        # Better solution 
        # n = len(nums)
        # r = k%n
        # self.reverse(nums , 0 , n-r-1)
        # self.reverse(nums , n -r , n-1)
        # self.reverse(nums , 0 , n-1)

        # Best Solutuion
        n = len(nums)
        r = k%n
        nums[:] = nums[n-r:]+ nums[:n-r]
        
        # Brute Force solution
        # for _ in range(0,r):
        #     e = nums.pop()
        #     nums.insert(0,e)


        # my solution
        # j = 1
        # while j<=r:
        #     nums[:] = [nums[-1]] + nums[0:n-1]
        
