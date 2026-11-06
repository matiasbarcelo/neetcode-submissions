class MinStack:

    def __init__(self):
        self.stack = []
        # there should be a prev_minimum and prev_minimum_count stack
        self.prev_minimum_stack = []
        self.minimum = None
        self.minimum_count = 0
                

    def push(self, val: int) -> None:
        # add to the stack obv
        self.stack.append(val)

        # if it's the first val
        if self.minimum == None:
            self.minimum = val
            self.minimum_count = 1
            return
        
        # if it's the same as minimum, add to count
        if val == self.minimum:
            self.minimum_count += 1

        # if it's less than the current minimum
        if val < self.minimum:
            # send the current minimum to the prev_minimum gulag with its count
            self.prev_minimum_stack.append((self.minimum, self.minimum_count))

            # then make the current val minimum and reset count to 1
            self.minimum = val
            self.minimum_count = 1

    def pop(self) -> None:
        val = self.stack.pop()
        # if it's the first val/stack is empty
        if not self.stack:
            self.minimum = None
            return
        
        # if it's equal to the current minimum and it's count is zero
        if val == self.minimum:
            self.minimum_count -= 1
        
        if self.minimum_count == 0:
            # out of the gulag
            prev_minimum, prev_minimum_count = self.prev_minimum_stack.pop()
            self.minimum = prev_minimum
            self.minimum_count = prev_minimum_count

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
        
