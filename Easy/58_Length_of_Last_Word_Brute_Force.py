class Solution(object):
    def lengthOfLastWord(self, s):
        high = len(s)-1
        while high>=0 and s[high] == ' ':
            high -=1
        length = 0
        while high>=0 and s[high] != ' ':
            length +=1
            high -=1
        return length
