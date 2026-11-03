class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        low = 0
        high = 0
        count = 0
        while high <len(s):
            if high-low + 1 == 3:
                if s[low] != s[low+1] and s[low+1] != s[high] and s[high] != s[low]:
                    count+=1
                low+=1
            high+=1
        return count
