from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        answer = 0
        product = 1
        
        for right in range(len(nums)):
            product *= nums[right]
            
            if product >= k:
                while product >= k and left <= right:
                    product /= nums[left]
                    left += 1
            
            answer += right - left + 1
        
        return answer