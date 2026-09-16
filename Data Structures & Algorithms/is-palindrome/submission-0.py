class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = "".join(char for char in s if char.isalnum())
        cleanS = cleanS.lower()
        i, j = 0, len(cleanS) - 1

        while i < j:
            if cleanS[i] != cleanS[j]: 
                print(cleanS[i], cleanS[j])
                return False
            i += 1
            j -= 1
        
        return True