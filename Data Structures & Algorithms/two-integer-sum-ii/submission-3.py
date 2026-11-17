class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_index = 0
        r_index = len(numbers) - 1

        while l_index < r_index:
            l_num = numbers[l_index]
            r_num = numbers[r_index]
            l_r_sum = l_num + r_num

            if l_r_sum == target:
                return [l_index + 1, r_index + 1]
            
            elif l_r_sum > target:
                r_index -= 1    
            elif l_r_sum < target:
                l_index += 1