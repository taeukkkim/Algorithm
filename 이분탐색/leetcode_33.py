from typing import List

# 풀이 1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1

# 풀이 2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        k = -1
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                k = i
                break
                
        if k == -1:
            return self.searchRange(nums, target)
        
        left_nums = nums[:k]
        right_nums = nums[k:]

        if target <= right_nums[-1]:
            result = self.searchRange(right_nums, target) 
            return len(left_nums) + result if result != -1 else -1
        else:
            return self.searchRange(left_nums, target)


    def searchRange(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            print(mid)

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1