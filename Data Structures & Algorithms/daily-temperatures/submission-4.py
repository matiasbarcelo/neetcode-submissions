class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        index_stack = []
        next_temp = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # on the first turn
            if not index_stack:
                index_stack.append(i)
                continue
            
            # otherwise
            prev_index = index_stack[-1]

            while temperatures[prev_index] < temperatures[i]:
                index_stack.pop()
                next_temp[prev_index] = (i + 1) - (prev_index + 1)
                if index_stack:
                    prev_index = index_stack[-1]
                else:
                    break
                    
            index_stack.append(i)
        
        return next_temp