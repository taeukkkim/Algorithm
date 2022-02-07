from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = left = 0
        answer = len(nums) + 1
        
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                answer = min(answer, i-left+1)
                total -= nums[left]
                left += 1
            
        return 0 if answer == len(nums) + 1 else answer