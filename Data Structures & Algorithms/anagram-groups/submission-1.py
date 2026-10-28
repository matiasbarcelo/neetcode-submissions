class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # o(n)
        # Create tuples of the strings with their indexes
        pairs = [(x, i) for i, x in enumerate(strs)]

        # with some accounting this is o(n)
        # reorder the chars in each string to alphabetical order
        pairs = [("".join(sorted(x)), i)for x, i in pairs]

        # o(n*log(n))
        # Sort the tuples now by their 0 index reordered chars
        pairs = sorted(pairs)

        # get the first pair
        last_pair = pairs[0]
        tl = []
        l1 = []

        # o(n)
        # group together the anagrams
        for n in range(len(pairs)):
            # skip the first iteration
            if n == 0:
                # edge case where there literally is only one str in strs
                if len(pairs) == 1:
                    l1.append([strs[0]])
                continue

            # get the values of two pairs
            last_pair_str = last_pair[0]
            last_pair_index = last_pair[1]
            current_pair_str = pairs[n][0]
            current_pair_index = pairs[n][1]

            # add the last pair's original str to temporary list
            tl.append(strs[last_pair_index])

            # if the current pairs str isn't the same as the last one
            if current_pair_str != last_pair_str:
                # add the temporary list to the big boy l1 list
                l1.append(tl)
                # and reset the temporary list
                tl = []
            
            # set last pair to the current pair
            last_pair = pairs[n]

            # on the last iteration
            if n == range(len(pairs))[-1]:
                # add the last original str to the temporary list
                tl.append(strs[current_pair_index])
                # then to the big boy l1 list
                l1.append(tl)
                # and break out of the loop in case it doesn't already
                break

        # o(n) with some accounting
        # The output expects the big boy list to have their lists of str ordered
        final_list = [sorted(str_list) for str_list in l1]

        return final_list


