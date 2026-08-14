class Solution(object):
    def numIdenticalPairs(self, nums):
        c = 0
        for i , d in enumerate(nums):
            for j , x in enumerate(nums):
                if d == x and i != j and i < j:
                    c +=1
        return c
