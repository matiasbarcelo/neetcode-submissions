from collections import defaultdict

class Solution:

    def __init__(self):
        # have a hash that keeps sets for row, column, and sub-boxes
        self.sodoku_hash = defaultdict(set)
        self.lim1 = 3
        self.lim2 = 6

    def reset_sodoku_hash(self) -> None:
        self.sodoku_hash = defaultdict(set)

    def is_in_sodoku_hash(self, row_key: str, column_key: str, subbox_key: str, num_str: str) -> bool:
        # convert num_str to int
        num_int = int(num_str)

        # Check if num is in any of these keys, if so return True
        if num_int in self.sodoku_hash[row_key] or num_int in self.sodoku_hash[column_key] or num_int in self.sodoku_hash[subbox_key]:
            return True

        # Otherwise add them to the hash and return False
        self.sodoku_hash[row_key].add(num_int)
        self.sodoku_hash[column_key].add(num_int)
        self.sodoku_hash[subbox_key].add(num_int)

        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we have to account for the rows, columns, and sub boxes
        row_num = 1 # this would be the item in the list
        column_num = 1 # this would be the index of each item num

        row_subbox_str = "r3"
        column_subbox_str = "c3"

        # we have n or 9 rows
        for row_list in board:

            row_key = "r" + str(row_num)

            if row_num > self.lim1:
                if row_num > self.lim2:
                    row_subbox_str = "r9"
                else:
                    row_subbox_str = "r6"
            
            # with m or 9 columns, m = n
            for column_str in row_list:

                if column_str.isdigit():
                    column_key = "c" + str(column_num)
                    
                    if column_num > self.lim1:
                        if column_num > self.lim2:
                            column_subbox_str = "c9"
                        else:
                            column_subbox_str = "c6"
                    
                    subbox_key = row_subbox_str + column_subbox_str

                    hash_result = self.is_in_sodoku_hash(row_key, column_key, subbox_key, column_str)

                    # if its in there, reset the hash and return false
                    if hash_result:
                        self.reset_sodoku_hash()
                        return False
                
                # add to column num
                column_num += 1
            
            # reset column stuff
            column_subbox_str = "c3"
            column_num = 1
            # add to row num
            row_num += 1

        # O(n^2) solution since m = n

        # if it's gotten through all the rows, reset the hash and return false
        self.reset_sodoku_hash()
        return True