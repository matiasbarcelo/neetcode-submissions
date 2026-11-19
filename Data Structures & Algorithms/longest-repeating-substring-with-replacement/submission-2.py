from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_rep = 1
        if len(s) == 1:
            return max_rep

        char_hash = defaultdict(int)
        char_hash[s[0]] += 1

        l_pointer = 0
        r_pointer = 1
        left_move_last_iter = False

        while r_pointer <= len(s) - 1:
            r_char = s[r_pointer]
            
            if not left_move_last_iter:
                char_hash[r_char] += 1
            
            len_so_far = r_pointer - l_pointer + 1
            highest_frequency_char = max(char_hash.values())

            calc = len_so_far - highest_frequency_char

            if calc > k:
                l_char = s[l_pointer]
                char_hash[l_char] -= 1
                l_pointer += 1
                left_move_last_iter = True
            else:
                if len_so_far > max_rep:
                    max_rep = len_so_far
                r_pointer += 1
                left_move_last_iter = False

        return max_rep