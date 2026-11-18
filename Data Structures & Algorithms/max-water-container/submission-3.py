class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        l_pointer = 0
        r_pointer = len(heights) - 1

        while l_pointer < r_pointer:
            l_num = heights[l_pointer]
            r_num = heights[r_pointer]
            
            length = min(l_num, r_num)
            width = r_pointer - l_pointer
            area = length * width
            
            if area > max_area:
                max_area = area
    
            if r_num > l_num :
                l_pointer += 1
            else:
                r_pointer -= 1

        return max_area