class Solution(object):
    def heightChecker(self, heights):
        pre = heights[:]
        n = len(pre)
        for i in range(0,n):
            mi = i
            for j in range(i+1 , n):
                if pre[j]<pre[mi]:
                    mi = j
            pre[i],pre[mi]=pre[mi],pre[i]

        count = 0
        for i in range (n):
            if heights[i] != pre[i]:
                count +=1
        return count
        
