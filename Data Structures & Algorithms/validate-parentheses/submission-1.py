from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        open_chars_stack = deque()
        open_bracket_set = set(["{","[","("])

        for char in s:
            # if it's an open bracket 
            if char in open_bracket_set:
                # add it to the stack
                open_chars_stack.append(char)
                continue
            
            # if it gets past that then it needs to be a close char
            # if there is nothing in the stack then its obv false
            if not open_chars_stack:
                return False
            
            # get the open bracket otherwise
            current_open_bracket = open_chars_stack.pop()

            # let's just do the three options
            if current_open_bracket == "{":
                if char != "}":
                    return False
                else:
                    continue
            elif current_open_bracket == "[":
                if char != "]":
                    return False
                else:
                    continue
            elif current_open_bracket == "(":
                if char != ")":
                    return False
                else:
                    continue
        
        if not open_chars_stack:
            return True
        else:
            return False