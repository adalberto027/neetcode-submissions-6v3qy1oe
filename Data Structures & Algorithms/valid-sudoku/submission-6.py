class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] in seen and board[i][j] != '.':
                    return False
                else:
                    seen.add(board[i][j])
            seen = set()

        for i in range(9):
            for j in range(9):
                if board[j][i] in seen and board[j][i] != '.':
                    return False
                else:
                    seen.add(board[j][i])
            seen = set()


        for x in range(0,9,3):
            for z in range(0,9,3):
                for i in range(3):
                    for j in range(3):
                        if board[i + x][j + z] in seen and board[i + x][j + z] != '.':
                            print(3)
                            return False
                        else:
                            seen.add(board[i + x][j + z]) 
                seen = set()

        return True