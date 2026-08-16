class Solution(object):
    def isPalindrome(self, s):
        x = "".join(filter(unicode.isalnum , s))
        x = lower(x)
        return self.pali(x, 0 , len(x)-1)
    def pali(self, x , l , r):
        if l>=r:
            return True
        if x[l] != x[r]:
            return False
        return self.pali(x, l + 1 , r-1)
