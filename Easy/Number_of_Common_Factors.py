class Solution(object):
    def commonFactors(self, a, b):
        r = [a]
        # r.append(a)
        for i in range(1 , (a//2) +1):
            if a % i == 0:
                r.append(i)
        

        rb = [b]
        # rb.append(b)
        for i in range(1 , (b//2)+1):
            if b % i == 0:
                rb.append(i)
        
        k = 0
        for i in r:
            for j in rb:
                if i == j:
                    k= k+1
        return k
