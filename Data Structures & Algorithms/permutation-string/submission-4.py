from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Two edge cases

        if s1 == "":
            return True
        
        if len(s1) == 1:
            if s1 in s2:
                return True
            else:
                return False
        
        # count hash for chars in s1
        count_s1 = Counter(s1)
        # find the amount of unique chars
        unique_char_count = len(count_s1.keys())
        # we will keep track of how many unique chars we've found the total count for
        found_so_far = 0

        # hash for char contains list of latest_index and count
        current_hash = {}

        l_pointer = 0
        r_pointer = 0

        while r_pointer <= len(s2) - 1:
            # get the right char
            r_char = s2[r_pointer]

            # if it's in s1
            if r_char in s1:
                # get the total count for s1
                s1_count = count_s1[r_char]
                # find out if it's already in the current hash
                retrieve_list = current_hash.get(r_char)
                curr_count = None

                # if it is
                if retrieve_list:
                    # figure out what the current count would be
                    curr_count = retrieve_list + 1

                    # if it's more than the total count, move the left pointer until it removes
                    # the current right char and then continue the algorithm
                    if curr_count > s1_count:
                        # looking for first occurance of r_char
                        
                        # I also have to decrease the count inbetween??
                        while s2[l_pointer] != r_char:
                            l_char = s2[l_pointer]
                            
                            if l_char in s1:
                                s1_l_char_count = count_s1[l_char]
                                s2_l_char_count = current_hash[l_char]
                                
                                if s1_l_char_count == s2_l_char_count:
                                    found_so_far -= 1

                                if s2_l_char_count == 1:
                                    del current_hash[l_char]
                                else:
                                    current_hash[l_char] -=1

                            l_pointer += 1
                        
                        # we found it
                        if current_hash[r_char] == 1:
                            del current_hash[r_char]
                        else:
                            current_hash[r_char] -=1

                        # increase l_pointer
                        l_pointer += 1
                        found_so_far -= 1

                        continue
                    
                    # and otherwise just update the entry count  
                    current_hash[r_char] += 1   
                
                # if it's not in the hash just instantiate it
                else:
                    # save the index of the first time this appears
                    current_hash[r_char] = 1
                    curr_count = 1
                
                # Need some logic to determine if current char finds permutation
                if curr_count == s1_count:
                    found_so_far += 1
                
                if found_so_far == unique_char_count:
                    return True
                
            else:
                new_index = r_pointer + 1
                found_so_far = 0
                current_hash = {}
            
            r_pointer += 1
            

        # if it gets through the whole thing than obv false
        return False
