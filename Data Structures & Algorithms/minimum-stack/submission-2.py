class MinStack:

    def __init__(self):
        self.stack = []
        # there should be a minimum hash
        # take [5,5,4,4,7,4,3,5] for example
        # {3:[4,1], 4:[5,3], 5:[None,3]}
        # Notice 7 is never in the hash table bc it was never min
        # first element is the prev minimum, second is self count
        # I guess technically you only have to keep track of its self count when it was min?
        self.minimum_hash = {}
        self.minimum = None
                

    def push(self, val: int) -> None:
        # add to the stack obv
        self.stack.append(val)
        # if it's the first val
        if self.minimum == None:
            self.minimum = val
            self.minimum_hash[val] = [None, 1]
        # if it's in the min hash you have to add to it's count?
        if val in self.minimum_hash:
            self.minimum_hash[val][1] += 1
        # if it's less than the current minimum
        if val < self.minimum:
            # initialize it in the hash with it's prev_minimum and with a count of 1
            self.minimum_hash[val] = [self.minimum, 1]
            # then make it min
            self.minimum = val

    def pop(self) -> None:
        val = self.stack.pop()
        # if it's the first val/stack is empty
        if not self.stack:
            self.minimum = None
            del self.minimum_hash[val]
        # if it's in the min hash you have to remove from it's count
        if val in self.minimum_hash:
            self.minimum_hash[val][1] -= 1
        # if it's equal to the current minimum and it's count is zero
        if val == self.minimum and self.minimum_hash[val][1] == 0:
            # we have a new minimum
            self.minimum = self.minimum_hash[val][0]
            del self.minimum_hash[val]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
        
