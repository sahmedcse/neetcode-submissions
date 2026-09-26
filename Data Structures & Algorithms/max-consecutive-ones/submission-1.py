class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount, currCount, isPrevOne = 0, 0, False 

        for n in nums:
            print(n, currCount)
            if n == 1:
                currCount += 1
            else:
                maxCount = max(maxCount, currCount)
                currCount = 0
            
            isPrevOne = n == 1
        
        return max(maxCount, currCount)
