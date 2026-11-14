class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_list = []
        post_list = [0] * len(nums)
        output = []

        num_so_far_pre = 1
        num_so_far_post = 1
        
        # make pre and post lists O(n)
        for i in range(len(nums)):
            post_index = i + 1
            pre_list.append(nums[i] * num_so_far_pre)
            post_list[-post_index] = nums[-post_index] * num_so_far_post

            # update pre and post num so far
            num_so_far_pre = pre_list[i]
            num_so_far_post = post_list[-post_index]

        for i in range(len(nums)):
            pre_index = i - 1
            post_index = i + 1

            if pre_index < 0:
                pre_num = 1
                post_num = post_list[post_index]
            elif post_index > len(nums) - 1:
                pre_num = pre_list[pre_index]
                post_num = 1
            else:
                pre_num = pre_list[pre_index]
                post_num = post_list[post_index]

            output.append(pre_num*post_num)

        return output

