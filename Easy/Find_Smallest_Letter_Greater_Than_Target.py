class Solution(object):
    def nextGreatestLetter(self, letters, target):
        n = len(letters)
        low = 0
        high = n-1
        ub = letters[0]
        while low<=high:
            mid = (low+high)//2
            if letters[mid]>target:
                ub = letters[mid]
                high = mid-1
            else:
                low = mid+1
        return ub
