class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in visited:
                return [visited[remainder], i]
            
            visited[nums[i]] = i