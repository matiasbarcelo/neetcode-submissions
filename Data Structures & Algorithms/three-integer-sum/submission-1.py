from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # list of all the nums that add up to zero
        true_list = []

        # sorting it is o(nlogn)
        nums = sorted(nums)
        
        for i in range(len(nums)):
            i_num = nums[i]
            target = -i_num
            j_pointer = i + 1
            k_pointer = len(nums) - 1
            
            while j_pointer < k_pointer:
                j_num = nums[j_pointer]
                k_num = nums[k_pointer]
                j_k_sum = j_num + k_num

                if j_k_sum == target:
                    curr_list = [i_num, j_num, k_num]
                    if curr_list not in true_list:
                        true_list.append(curr_list)
                    k_pointer -= 1
                    j_pointer += 1
                    continue
            
                elif j_k_sum > target:
                    k_pointer -= 1
                elif j_k_sum < target:
                    j_pointer += 1

        return true_list