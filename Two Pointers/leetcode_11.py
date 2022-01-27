from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_width = len(height)-1
        answer = 0
        
        for width in range(max_width, 0, -1):
            if height[left] < height[right]:
                answer = max(answer, width * height[left])
                left += 1
            else:
                answer = max(answer, width * height[right])
                right -= 1
                
        return answer