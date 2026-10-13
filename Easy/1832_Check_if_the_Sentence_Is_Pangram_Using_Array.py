class Solution(object):
    def checkIfPangram(self, sentence):
        n = len(sentence)
        arr = [0] * 26
        for i in range(0,n):
            asscii_value = ord(sentence[i])
            index = asscii_value - 97
            arr[index] = 1
        for i in range(0,26):
            if arr[i] == 0:
                return False
        return True
