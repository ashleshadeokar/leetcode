class Solution:
    def solve(self, board: list[list[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def bfs():
            q = deque()
            for r in range(rows):
                for c in range(cols):
                    if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == "O":
                        q.append((r, c))
            
            while q:
                r, c = q.popleft()
                if board[r][c] == "O":
                    board[r][c] = "T"
                    for dx, dy in directions:
                        nr, nc = r + dx, c + dy
                        if 0 <= nr < rows and 0 <= nc < cols:
                            q.append((nr, nc))

        bfs()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"