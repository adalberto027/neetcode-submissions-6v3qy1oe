class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for e in board:
            temp = set()
            for j in e:
                if j != '.':
                    if int(j) in temp or int(j) > 9 or int(j) < 0:
                        print(1, int(j) in temp, int(j) < 9, int(j) < 0)
                        return False
                    else:
                        temp.add(int(j))
        
        for i in range(len(board[0])):
            temp = set()
            for j in range(len(board)):
                if board[j][i] != '.':
                    if int(board[j][i]) in temp or int(board[j][i]) > 9 or int(board[j][i]) < 0:
                        print(2)
                        return False
                    else:
                        temp.add(int(board[j][i]))
        
        for z in range(0,7,3):
            for x in range(0,7,3):
                temp = set()
                for i in range(0+x, 3+x):
                    for j in range(0+z,3+z):
                        if board[i][j] != '.':
                            if int(board[i][j]) in temp or int(board[i][j]) > 9 or int(board[i][j]) < 0:
                                print(temp, board[i][j], i, j, int(board[i][j]) in temp, int(board[i][j]) > 9, int(board[i][j]) < 0)
                                return False
                            else:
                                temp.add(int(board[i][j]))
                    

        return True