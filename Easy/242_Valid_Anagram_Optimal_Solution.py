class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = [0] * 26
        if len(s) != len(t):
            return False
        for i in s:
            ascii_value = ord(i)
            index = ascii_value - 97
            hm[index] +=1
        for j in t:
            ascii_value = ord(j)
            index = ascii_value - 97
            if hm[index] == 0:
                return False
            hm[index]-=1
        return True
