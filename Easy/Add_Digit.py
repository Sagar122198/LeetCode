class Solution(object):
    def addDigits(self, num):
        r = 0
        if num == 0:
            return 0
        while num>0:
            ld = num % 10
            r = r + ld
            num = num//10
            if num == 0:
                if len(str(r)) == 1:
                    return r
                else:
                    num=r
                    r=0
