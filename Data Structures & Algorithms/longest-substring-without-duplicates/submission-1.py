import bisect
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        l_index = 0
        max_amount = 1
        current_substring = s[0]
        longest_string = current_substring

        # make a hash table with the indexes of each char
        char_hash = defaultdict(list)

        # we can binary search the hash table later
        for n in range(len(s)):
            char_hash[s[n]].append(n)

        # for our right pointer up to the end of the string
        for i in range(len(s) - 1):
            # we want the r index for sliding window, which is i + 1
            i = i + 1
            r = s[i]

            # check to see if it's in the substring
            # I guess this is O(n), but there are a limited amount of possible chars k?
            if r in current_substring:
                # find the left index by doing a binary search on the hash table result for r
                # the index should be one less than the bisect left i, and our new left pointer will be
                # that looked up index + 1, this is o(logn)
                index_of_index = bisect.bisect_left(char_hash[r], i) - 1
                # we want to be just 1 after that
                l_index = char_hash[r][index_of_index] + 1
                current_substring = s[l_index:i + 1]
                continue
            else:
                current_substring = s[l_index:i + 1]

            calc = i - l_index + 1

            if calc > max_amount:
                max_amount = calc
                longest_string = s[l_index:i + 1]

        return max_amount