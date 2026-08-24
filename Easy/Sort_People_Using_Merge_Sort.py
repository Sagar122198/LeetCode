class Solution(object):
    def merge_array(self, left, right):
        result = []
        i,j = 0,0
        n,m=len(left),len(right)
        while i<n and j<m:
            if left[i] <= right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        while i<n:
            result.append(left[i])
            i+=1
        while j<m:
            result.append(right[j])
            j+=1
        return result
    def merge_sort(self,heights):
        n = len(heights)
        if n == 1:
                return heights
        mid = n//2
        left_arr = heights[:mid]
        right_arr =heights[mid:]
        left=self.merge_sort(left_arr)
        right = self.merge_sort(right_arr)
        return self.merge_array(left,right)
    def sortPeople(self, names, heights):
        dic = dict(zip(heights,names))
        
        result = self.merge_sort(heights)
        result.reverse()
        return [dic[key] for key in result]
