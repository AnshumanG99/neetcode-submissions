class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        


        colset = {}
        rowset = {}
        boxset = {}

        for r in range(len(board)):
            for c in range(len(board[0])):

                val = board[r][c]
                if val == ".":
                    continue

                if c not in colset:
                    colset[c] = set()
                
                if r not in rowset:
                    rowset[r] = set()
                
                if (r // 3, c // 3) not in boxset:
                    boxset[r // 3, c // 3] = set()

                if val in colset[c] or val in rowset[r] or val in boxset[r // 3, c // 3]:
                    return False


                colset[c].add(val)
                rowset[r].add(val) 
                boxset[r // 3, c // 3].add(val)

        return True