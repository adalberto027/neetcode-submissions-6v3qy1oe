class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0


        rows, colums  = len(grid), len(grid[0])
        visited = set()
        self.bigestIsland = 0
        self.temp  = 0

        def bfs(r, c):
            self.temp  += 1
            self.bigestIsland = max(self.bigestIsland, self.temp)
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions  = [[1,0], [0,1], [-1, 0], [0,-1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(colums) and grid[r][c] == 1 and (r, c) not in visited:
                        self.temp += 1
                        self.bigestIsland = max(self.bigestIsland, self.temp)
                        q.append((r, c))
                        visited.add((r, c))
        for i in range(rows):
            for j in range(colums):
                if grid[i][j] == 1 and (i, j) not in visited:
                    bfs(i,j)
                    self.temp = 0
        return self.bigestIsland