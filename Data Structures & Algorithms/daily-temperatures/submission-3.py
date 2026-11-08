class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temperatures[0] = 30 [0] [0, 0, 0, 0, 0, 0, 0] turn 1
        # temperatures[1] = 38 [1] [1, 0, 0, 0, 0, 0, 0] turn 2
        # temperatures[2] = 30 [1, 2] [1, 0, 0, 0, 0, 0, 0] turn 3
        # temperatures[3] = 36 [1, 3] [1, 0, 1, 0, 0, 0, 0] turn 4
        # temperatures[4] = 35 [1, 3, 4] [1, 0, 1, 0, 0, 0, 0] turn 5
        # temperatures[5] = 40 [5] [1, 4, 1, 2, 1, 0, 0] turn 6
        # temperatures[6] = 28 [5, 6] [1, 4, 1, 2, 1, 0, 0] turn 7

        # return [1, 4, 1, 2, 1, 0, 0]

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