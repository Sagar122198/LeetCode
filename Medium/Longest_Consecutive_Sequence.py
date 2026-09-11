class Solution(object):
    def longestConsecutive(self, nums):
        # Brute force and Optimal soluiton does not give TC -> of o(n)

        # Optimal Solution
        n = len(nums)
        my_set = set()
        for i in range(0,n):
            my_set.add(nums[i])
        longest = 0
        for num in my_set:
            if num-1 not in my_set:
                count = 1
                x = num
                while x+1 in my_set:
                    count +=1
                    x+=1
                longest = max(longest,count)
        return longest
