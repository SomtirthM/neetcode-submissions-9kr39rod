class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_checker = [set() for _ in range(9)]
        col_checker = [set() for _ in range(9)]
        box_checker = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == '.':
                    continue
                box_index = (r//3)*3 + (c//3)

                if val in row_checker[r] or val in col_checker[c] or val in box_checker[box_index]:
                    return False
            
                row_checker[r].add(val)
                col_checker[c].add(val)
                box_checker[box_index].add(val)
        
        return True
        