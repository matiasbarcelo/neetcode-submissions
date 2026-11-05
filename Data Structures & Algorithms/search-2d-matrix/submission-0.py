
class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_index_row = 0
        r_index_row = len(matrix) - 1
        
        # just do binary search twice
        while l_index_row <= r_index_row:
            m = (l_index_row + r_index_row) // 2
            l_index_inside = 0
            r_index_inside = len(matrix[m]) - 1

            while l_index_inside <= r_index_inside:
                m_inside = (l_index_inside + r_index_inside) // 2
                if matrix[m][m_inside] == target:
                    return True
                elif target > matrix[m][m_inside]:
                    l_index_inside = m_inside + 1
                elif target < matrix[m][m_inside]:
                    r_index_inside = m_inside - 1

            if target > matrix[m][0] :
                l_index_row= m + 1
            elif target < matrix[m][0]:
                r_index_row = m - 1
        
        return False