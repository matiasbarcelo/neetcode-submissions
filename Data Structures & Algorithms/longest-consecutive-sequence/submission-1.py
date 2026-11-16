class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        max_count = 1
        max_set = set()

        # O(n)
        for num in nums:
            # if it's in max set just go on to the next num
            if num in max_set:
                continue

            curr_count = 1
            curr_set = set([num])
            prev_num = num - 1
            next_num = num + 1

            # find all the consecutive prev_nums
            while prev_num in nums_set:
                curr_count += 1
                curr_set.add(prev_num)
                prev_num -= 1

            # find all the consecutive next_nums
            while next_num in nums_set:
                curr_count += 1
                curr_set.add(next_num)
                next_num += 1

            if curr_count > max_count:
                max_count = curr_count
                max_set = curr_set
            
        return max_count