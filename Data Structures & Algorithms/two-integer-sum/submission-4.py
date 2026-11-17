from collections import defaultdict, deque

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index_hash = defaultdict(deque)

        for ind in range(len(nums)):
            num = nums[ind]
            index_hash[num].append(ind)

        sorted_nums = sorted(nums)

        j_sorted = len(nums) - 1
        i_sorted = 0

        while i_sorted < j_sorted:
            i_num = sorted_nums[i_sorted]
            j_num = sorted_nums[j_sorted]
            i_j_sum = i_num + j_num

            if i_j_sum == target:
                nums_index_i = index_hash[i_num].popleft()
                nums_index_j = index_hash[j_num].popleft()
                return sorted([nums_index_i, nums_index_j])

            elif i_j_sum > target:
                j_sorted -= 1
            
            elif i_j_sum < target:
                i_sorted += 1