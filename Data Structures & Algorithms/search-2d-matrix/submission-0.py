class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarysearch(l: List[int], target: int) -> bool:
            p1, p2 = 0, len(l)-1

            while p1 <= p2:
                m = int((p1+p2)/2)
                if l[m] == target:
                    return True
                if l[m] > target:
                    p2 = m - 1
                else:
                    p1 = m + 1
            return False
        ans = False

        for e in matrix:
            ans = ans or binarysearch(e, target)
        
        return ans

        

        