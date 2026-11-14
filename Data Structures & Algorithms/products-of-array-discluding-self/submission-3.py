class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        grand_multiple = 1
        zero_index = None

        # o(n) to find the index of the zero if it's there
        # also find grand multiple of nums
        for i in range(len(nums)):
            # if zero_index doesn't have a val yet & the current index for nums is zero
            if nums[i] == 0 and zero_index == None:
                zero_index = i
                continue
            
            grand_multiple = grand_multiple * nums[i]

        return_list = [0] * len(nums)

        # if zero index exists, just return make the zero_index the grand multiple
        # and return the return list. This works for count of zero >= 1
        if zero_index != None:
            # grand_multiple will just be zero if more than one zero so it changes nothing
            return_list[zero_index] = grand_multiple
            return return_list

        # Otherwise just go through the list and divide the grand multiple by nums[i]
        # O(n)
        for i in range(len(nums)):
            return_list[i] = grand_multiple // nums[i]
        
        # Aggregate analysis, O(n) + O(n) = O(n)
        return return_list