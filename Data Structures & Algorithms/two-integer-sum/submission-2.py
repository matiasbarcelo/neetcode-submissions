class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)

        R_index_sorted = len(nums) - 1
        L_index_sorted = 0

        # O(n)
        while L_index_sorted != R_index_sorted:
            if sorted_nums[L_index_sorted] + sorted_nums[R_index_sorted] == target:
                
                left_num = sorted_nums[L_index_sorted]
                right_num = sorted_nums[R_index_sorted]
                
                for n in range(len(nums)):
                    if nums[n] == left_num:
                        left_index = n
                        break
                
                for m in list(reversed(range(len(nums)))):
                    if nums[m] == right_num:
                        right_index = m
                        break
                
                return sorted([left_index, right_index])
            elif sorted_nums[L_index_sorted] + sorted_nums[R_index_sorted] > target:
                R_index_sorted = R_index_sorted - 1
            elif sorted_nums[L_index_sorted] + sorted_nums[R_index_sorted] < target:
                L_index_sorted = L_index_sorted + 1