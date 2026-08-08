class Solution(object):
    def reverse(self, x):
        new = 0
        if x>0:
            while x>0:
                ld = x % 10
                new = new * 10 + ld
                x = x//10
                if new < -2147483648 or new > 2147483647:
                    return 0
            return new
        else:
            x = x * -1
            while x>0:
                ld = x%10
                new = new * 10 +ld
                x= x//10
                if new < -2147483648 or new > 2147483647:
                    return 0
            return -new
