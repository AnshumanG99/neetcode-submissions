class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):

            vertvalues = []
            horivalues = []
            
            if i == 0 or i == 3 or i == 6:

                box1 = []
                box2 = []
                box3 = []

            for j in range(9):
                
                vertvalue = board[i][j]
                horivalue = board[j][i]

                if vertvalue.isdigit():
                    vertvalues.append(vertvalue)
                    if j <= 2:
                        box1.append(vertvalue)
                    elif j <= 5:
                        box2.append(vertvalue)
                    else:
                        box3.append(vertvalue)                    

                if horivalue.isdigit():
                    horivalues.append(horivalue)
            
            if i == 2 or i == 5 or i == 8:
                box1set = set(box1)
                box2set = set(box2)
                box3set = set(box3)
                if not len(box1) == len(box1set) or not len(box2) == len(box2set) or not len(box3) == len(box3set):
                    return False

            if not len(vertvalues) == len(set(vertvalues)) or not len(horivalues) == len(set(horivalues)):
                return False
        
        return True


