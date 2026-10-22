class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        pacific = atlantic = False

        def dfs(r, c, val):
            nonlocal atlantic, pacific
            if r < 0 or c < 0:
                pacific = True
                return
            if r >= rows or c >= cols:
                atlantic = True
                return
            if heights[r][c] > val:
                return

            tmp = heights[r][c]
            heights[r][c] = float('inf')
            for dx, dy in directions:
                dfs(r + dx, c + dy, tmp)
                if pacific and atlantic:
                    break
            heights[r][c] = tmp

        res = []
        for r in range(rows):
            for c in range(cols):
                pacific = False
                atlantic = False
                dfs(r, c, float('inf'))
                if pacific and atlantic:
                    res.append([r, c])
        return res