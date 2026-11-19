class Solution:
    def backward_brack(self, s: str, k: int, r_pointer: int):
        rep_so_far = 1
        rep_char = s[r_pointer]
        non_count = 0
        curr_char_hash = {rep_char: 1}
        l_pointer = r_pointer - 1

        while l_pointer >= 0:
            l_char = s[l_pointer]

            if l_char == rep_char:
                # rep count is in curr_char_hash
                curr_char_hash[rep_char] += 1
                calc = curr_char_hash[rep_char] + non_count
                if calc > rep_so_far:
                    rep_so_far = calc
                l_pointer -= 1
                continue

            look_up_r_char = curr_char_hash.get(l_char)

            if look_up_r_char == None:
                non_count += 1
                curr_char_hash[l_char] = 1
            else:
                non_count += 1
                curr_char_hash[l_char] += 1

            if curr_char_hash[l_char] > curr_char_hash[rep_char]:
                rep_char = l_char
                non_count -= 1

            if non_count > k:
                non_count -= 1
                l_char_count = curr_char_hash[l_char]
                
                if l_char_count == 1:
                    del curr_char_hash[l_char]
                else:
                    curr_char_hash[l_char] -= 1

                return rep_so_far, rep_char, non_count, curr_char_hash
            
            else:
                calc = curr_char_hash[rep_char] + non_count
                if calc > rep_so_far:
                    rep_so_far = calc
                    
            l_pointer -= 1
        
        return rep_so_far, rep_char, non_count, curr_char_hash

    def forward_brack(self, s: str, k: int, l_pointer: int, rep_so_far, rep_char, non_count, curr_char_hash):
        max_rep = rep_so_far
        r_pointer = l_pointer + 1

        while r_pointer <= len(s) - 1:
            r_char = s[r_pointer]

            if r_char == rep_char:
                # rep count is in curr_char_hash
                curr_char_hash[rep_char] += 1
                calc = curr_char_hash[rep_char] + non_count
                if calc > max_rep:
                    max_rep = calc
                r_pointer += 1
                continue

            look_up_r_char = curr_char_hash.get(r_char)

            if look_up_r_char == None:
                non_count += 1
                curr_char_hash[r_char] = 1
            else:
                non_count += 1
                curr_char_hash[r_char] += 1

            if curr_char_hash[r_char] > curr_char_hash[rep_char]:
                rep_char = r_char
                non_count -= 1

            if non_count > k:
                return max_rep, r_pointer
            
            else:
                calc = curr_char_hash[rep_char] + non_count
                if calc > max_rep:
                    max_rep = calc
                    
            r_pointer += 1
        
        return max_rep, r_pointer


    def characterReplacement(self, s: str, k: int) -> int:
        max_rep = 1
        r_pointer = 0
        
        while r_pointer <= len(s) - 1:
            rep_so_far, rep_char, non_count, curr_char_hash = self.backward_brack(s, k, r_pointer)
            curr_rep, r_pointer = self.forward_brack(s, k, r_pointer, rep_so_far, rep_char, non_count, curr_char_hash)
            if curr_rep > max_rep:
                max_rep = curr_rep

        return max_rep