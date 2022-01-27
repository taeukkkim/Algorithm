from typing import List

# 풀이 1: 파이썬기능 써봄
import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        
        return [bisect.bisect_left(nums,target), bisect.bisect_right(nums,target)-1]

# 풀이 2
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        
        return [self.searchLeft(nums, target), self.searchRight(nums, target)] 
    
    def searchLeft(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def searchRight(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right