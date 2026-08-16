class Solution(object):
    def reverseString(self, s):
        self.reverse( s , 0 ,len(s)-1)
    def reverse(self , s , l , r):
        if l >= r:
            return 
        s[l] , s[r] = s[r],s[l]
        self.reverse(s,l+1 , r-1)
