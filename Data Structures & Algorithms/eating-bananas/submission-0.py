import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_piles = max(piles)
        last_num_worked = None

        l_num = 1
        r_num = max_piles
        current_num = (r_num + l_num) // 2

        while l_num <= r_num:
            current_sum = 0

            for i in range(len(piles)):
                current_sum += math.ceil(piles[i]/current_num)
        
            if current_sum <= h:
                last_num_worked = current_num
                r_num = current_num - 1
                current_num = (r_num + l_num) // 2
            else:
                l_num = current_num + 1
                current_num = (r_num + l_num) // 2

        return last_num_worked

