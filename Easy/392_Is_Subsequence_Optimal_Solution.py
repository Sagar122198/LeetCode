class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        i =0 
        j = 0
        count = 0
        while i<m and j<n:
            if s[i] == t[j]:
                count +=1
                i+=1
                j+=1
            else:
                j+=1
        if count == m:
            return True
        else:
            return False
