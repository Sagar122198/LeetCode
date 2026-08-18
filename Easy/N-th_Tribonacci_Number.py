class Solution(object):
    def tribonacci(self, n):
        memo = {}

        def f(n):
            if n == 0 or n == 1:
                return n
            if n == 2:
                return 1

            if n in memo:
                return memo[n]

            memo[n] = f(n-1) + f(n-2) + f(n-3)
            return memo[n]

        return f(n)
