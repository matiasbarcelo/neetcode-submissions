import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            # already sorted oh
            l_index = 0
            r_index = len(nums) - 1
            while True:
                mid = l_index + math.ceil((r_index - l_index)/2)
                if nums[mid] == target:
                    return mid
                elif r_index == 1:
                    r_index = 0
                elif nums[mid] > target:
                    r_index = mid
                else:
                    l_index = mid
        else:
            return -1