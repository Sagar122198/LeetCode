class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        positive_list= []
        negative_list = []
        rearranged_list = []
        for i in range(0,n):
            if nums[i]>0:
                positive_list.append(nums[i])
            else:
                negative_list.append(nums[i])
        i, j = 0, 0
        for k in range(n):
            if k %2 == 0:
                rearranged_list.append(positive_list[i])
                i+=1
            else:
                rearranged_list.append(negative_list[j])
                j+=1
        return rearranged_list
