class Solution(object):
    def heightChecker(self, heights):
        pre = heights[:]
        n = len(pre)
        for i in range(1,n):
            key = pre[i]
            j = i-1
            while j>=0 and pre[j]>key:
                pre[j+1] = pre[j]
                j-=1
            pre[j+1] = key

        count = 0
        for i in range (n):
            if heights[i] != pre[i]:
                count +=1
        return count        
