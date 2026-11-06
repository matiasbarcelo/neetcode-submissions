class Solution:
    def isValid(self, s: str) -> bool:
        open_chars_stack = []
        open_bracket_set = {"{":"}", "[":"]", "(":")"}

        for char in s:
            # if it's an open bracket 
            if char in open_bracket_set.keys():
                # add it to the stack
                open_chars_stack.append(char)
                continue
            
            # if it gets past that then it needs to be a close char
            # if there is nothing in the stack then its obv false
            if not open_chars_stack:
                return False
            
            # get the open bracket otherwise
            current_open_bracket = open_chars_stack.pop()

            if char != open_bracket_set[current_open_bracket]:
                return False
        
        if not open_chars_stack:
            return True
        else:
            return False