class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map_magazine = [0] *26
        for i in magazine:
            ascii_value = ord(i)
            index = ascii_value - 97
            hash_map_magazine[index] +=1
        for j in ransomNote:
            ascii_value = ord(j)
            index = ascii_value - 97
            if hash_map_magazine[index] == 0:
                return False
            hash_map_magazine[index] -=1
        return True
