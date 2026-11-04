class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        l_index = 0
        max_amount = 1
        last_cut = 0

        # make a hash table with the indexes of each char
        char_hash = {s[l_index]: 0}

        # for our right pointer up to the end of the string
        for i in range(len(s) - 1):
            # we want the r index for sliding window, which is i + 1
            i = i + 1
            r = s[i]
            look_up = char_hash.get(r)
            char_hash[r] = i

            if look_up != None and look_up >= last_cut:
                last_cut = look_up
                l_index = look_up + 1
                continue

            calc = i - l_index + 1

            if calc > max_amount:
                max_amount = calc

        return max_amount
