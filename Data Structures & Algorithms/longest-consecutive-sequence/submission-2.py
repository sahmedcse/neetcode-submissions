import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        
        longest = 0
        currentLength = 0
        last = None

        while nums:
            current = heapq.heappop(nums)
            if last is None:
                currentLength = 1
            elif current == last + 1:
                currentLength += 1
            elif current > last:
                longest = max(currentLength, longest)
                currentLength = 1
            
            last = current
        
        return max(longest, currentLength)
