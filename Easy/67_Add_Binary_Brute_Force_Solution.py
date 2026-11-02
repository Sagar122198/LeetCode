class Solution:
    def addBinary(self, a: str, b: str) -> str:
        count = 0
        num1 = 0
        num2 = 0
        if a=="0" and b =="0":
            return "0"
        for i in range(len(a)-1,-1,-1):
            num1 += int(a[i])* (2**count)
            count +=1
        count = 0
        for j in range(len(b)-1,-1,-1):
            num2 += (2**count) * int(b[j])
            count +=1
        nums = num1+num2
        result = ""
        while nums>0:
            if nums%2 == 1:
                result += "1"
            else:
                result +="0"
            nums=nums//2
        result = result[::-1]
        return result
