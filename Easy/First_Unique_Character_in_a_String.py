class Solution(object):
    def firstUniqChar(self, s):
        hl = [0] * 26
        x = len(s)-1
        for i in s:
            av = ord(i)
            index = av - 97
            hl[index] += 1
        for i,ch in enumerate(s):
            av = ord(ch)
            index = av - 97
            if hl[index] == 1:
                return i
        else:
            return -1
