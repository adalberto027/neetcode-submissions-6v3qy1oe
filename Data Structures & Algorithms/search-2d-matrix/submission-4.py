class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        p1 = 0
        p2 = len(matrix) * len(matrix[0]) - 1

        while p1 <= p2:
            m = (p1 + p2) // 2
            if matrix[m // len(matrix[0])][m % len(matrix[0])] > target:
                p2 = m - 1
            elif matrix[m // len(matrix[0])][m % len(matrix[0])] < target:
                p1 = m + 1
            else:
                return True
        return False
        