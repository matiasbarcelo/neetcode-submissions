class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temperatures[0] = 30 [0] [1] [None, None, None, None, None, None, None] turn 1
        # temperatures[1] = 38 [1] [2] [1, None, None, None, None, None, None] turn 2
        # temperatures[2] = 30 [1, 2] [2, 3] [1, None, None, None, None, None, None] turn 3
        # temperatures[3] = 36 [1, 3] [2, 4] [1, None, 1, None, None, None, None] turn 4
        # temperatures[4] = 35 [1, 3, 4] [2, 4, 5] [1, None, 1, None, None, None, None] turn 5
        # temperatures[5] = 40 [5] [6] [1, 4, 1, 2, 1, None, None] turn 6
        # temperatures[6] = 28 [5, 6] [6, 7] [1, 4, 1, 2, 1, None, None] turn 7

        # [5] [6] [1, 4, 1, 2, 1, None, 0] clear remaining 1
        # [] [] [1, 4, 1, 2, 1, 0, 0] clear remaining 2

        # return [1, 4, 1, 2, 1, 0, 0]

        index_stack = []
        next_temp = [None] * len(temperatures)

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
        
        while index_stack:
            index = index_stack.pop()
            next_temp[index] = 0
        
        return next_temp