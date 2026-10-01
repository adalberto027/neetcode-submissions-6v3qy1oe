class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        numbers = {'1','2','3','4','5','6','7','8','9'}
        for row in board:
            for e in row:
                if e != '.':
                    if e not in numbers:
                        print(1,e, numbers)
                        return False
                    numbers.remove(e)
            numbers = {'1','2','3','4','5','6','7','8','9'}
        
        #Check cols
            for i in range(len(board)):
                for j in range(len(board[i])):
                    print(board[j][i])
                    e = board[j][i]
                    if e != '.':
                        if e not in numbers:
                            print(2)
                            return False
                        numbers.remove(e)
                        print('#') 
                numbers = {'1','2','3','4','5','6','7','8','9'}
        

        for i in range(0,9,3):

            for j in range(0,9,3):

                numbers = {'1','2','3','4','5','6','7','8','9'}
                for x in range(3):
                    for z in range(3):
                        if board[i+x][j+z] != '.':
                            if board[i+x][j+z] not in numbers:
                                return False
                            numbers.remove(board[i+x][j+z]) 
        return True


        

            

        