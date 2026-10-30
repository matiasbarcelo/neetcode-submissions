import bisect

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        set_nums = set(nums)
        dict_nums = {}

        for num in set_nums:
            dict_nums[num] = 0
        
        for num in nums:
            dict_nums[num] += 1

        k_list = []

        for num, count in dict_nums.items():
            if len(k_list) < k:
                if not k_list:
                    k_list.append((count, num))
                else:
                    insort_index  = bisect.bisect_right(k_list, count, key= lambda pair: pair[0])
                    k_list.insert(insort_index, (count, num))
            else:
                insort_index  = bisect.bisect_right(k_list, count, key= lambda pair: pair[0])
                if insort_index > 0:
                    k_list.insert(insort_index, (count, num))
                    k_list.pop(0)

        final_list = [tup[1] for tup in k_list]

        return final_list