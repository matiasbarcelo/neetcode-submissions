import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            # already sorted oh
            l_index = 0
            r_index = len(nums) - 1
            while True:
                mid = l_index + math.floor((r_index - l_index)/2)
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r_index = mid - 1
                else:
                    l_index = mid + 1
        else:
            return -1