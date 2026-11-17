class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digit = 0
        for i in range(0,len(digits)):
            digit= (digit*10)+digits[i]
        digit+=1
        result=[]
        for i in str(digit):
            result.append(int(i))   
        return result 