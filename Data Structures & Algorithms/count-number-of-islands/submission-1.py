class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, columns = len(grid), len(grid[0])
        seen = set()
        ans = 0

        def bfs(r, c):
            q = collections.deque()
            seen.add((r,c))
            q.append((r,c))
            while q:
                row, column = q.popleft()
                directions = [[1,0],[0,1], [-1,0],[0,-1]]
                for dr, dc in directions:
                    r, c = row + dr, column + dc
                    if r in range(rows) and c in range(columns) and grid[r][c] == '1' and (r, c) not in seen:
                        q.append((r,c))
                        seen.add((r,c))



        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1' and (i,j) not in seen:
                    bfs(i, j)
                    ans += 1

        return ans

                