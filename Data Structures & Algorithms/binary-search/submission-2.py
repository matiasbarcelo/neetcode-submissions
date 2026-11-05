import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        binary_search_index = bisect.bisect_left(nums, target)

        if binary_search_index <= len(nums) - 1 and nums[binary_search_index] == target:
            return binary_search_index
        else:
            return -1