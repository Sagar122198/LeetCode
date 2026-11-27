class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            total = 0
            while num>0:
                ld = num%10
                total += ld **2
                num = num//10
            return total
        slow = n
        fast = get_next(n)
        while fast !=1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        if fast == 1:
            return True
        else:
            return False
