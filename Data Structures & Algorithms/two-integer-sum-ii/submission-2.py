import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # set current index to the first index
        current_index = 0

        while current_index < len(numbers) - 1:
            # figure out your new_target by subtracting the current index num from the old_target
            new_target = target - numbers[current_index]
            # binary search the rest of the numbers
            nums_search_index = bisect.bisect_left(numbers, new_target, lo = current_index + 1)

            if nums_search_index < len(numbers) and numbers[nums_search_index] == new_target:
                # wants it "1-indexed" for some reason
                return [current_index + 1, nums_search_index + 1]
            current_index = bisect.bisect_right(numbers, numbers[current_index])
        
        return []