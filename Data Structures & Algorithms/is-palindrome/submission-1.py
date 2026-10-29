class Solution:
    def isPalindrome(self, s: str) -> bool:
         # get a left and right pointer
        l = 0
        r = len(s) - 1

        while l < r:
            l_alphanumeric = s[l].isalnum()
            r_alphanumeric = s[r].isalnum()

            if l_alphanumeric and r_alphanumeric:
                if not s[l].lower() == s[r].lower():
                    return False
                l = l + 1
                r = r - 1

            if not l_alphanumeric:
                l = l + 1
            
            if not r_alphanumeric:
                r = r - 1

        return True