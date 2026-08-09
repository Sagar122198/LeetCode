class Solution(object):
    def isPalindrome(self, x):
        com = x
        result = 0
        while x>0:
            ld = x % 10
            result = result * 10 + ld
            x = x// 10
        if result == com:
            return True
        else:
            return False
        
