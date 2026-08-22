class Solution(object):
    def heightChecker(self, heights):
        pre = heights[:]
        n = len(pre)
        for i in range(n-2 , -1 , -1):
            for j in range(0,i+1):
                if pre[j]>pre[j+1]:
                    pre[j],pre[j+1] = pre[j+1] , pre[j]

        count = 0
        for i in range (n):
            if heights[i] != pre[i]:
                count +=1
        return count
        
