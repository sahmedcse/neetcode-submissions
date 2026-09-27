class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap = {}

        for c in s:
            if c in charMap:
                charMap[c] += 1
            else:
                charMap[c] = 1
        
        for c2 in t:
            if c2 not in charMap or charMap[c2] <= 0:
                return False
            
            charMap[c2] -= 1
        
        for k, v in charMap.items():
            if v > 0:
                return False
        
        return True
            