class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        visited = set()

        def dfs(r, c):
            nonlocal max_area

            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0

            if (r, c) in visited:
                return 0

            area = 1

            visited.add((r, c))

            area = area + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

            max_area = max(max_area, area)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)

        return max_area
