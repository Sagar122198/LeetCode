class Solution(object):
    def findLucky(self, arr):
        hl = [0] * 501
        for i , d in enumerate(arr):
            hl[d]+=1
        l = -1
        for i in hl:
            if hl[i] == i and i !=0:
                if i > l:
                    l = i        
        else:
            return l
