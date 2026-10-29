class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create a new string
        alphanum_chars = []

        # check to see if the char is alphanumeric
        for c in s:
            if c.isalnum():
                alphanum_chars.append(c.lower())
        
        alphanum_str = "".join(alphanum_chars)
        alphanum_chars.reverse()
        reversed_alphanum_str = "".join(alphanum_chars)

        return alphanum_str == reversed_alphanum_str