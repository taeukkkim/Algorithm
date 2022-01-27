from typing import List

# 풀이 1
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_num = max(nums)
        return nums.index(max_num)

# 풀이 2: 이분탐색
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if (mid == 0 or nums[mid-1] < nums[mid]) and (mid == len(nums)-1 or nums[mid+1] < nums[mid]):
                return mid
            elif mid == 0 or nums[mid-1] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            
        return 0