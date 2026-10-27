class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        res = []
        for r in range(len(matrix[0])):
            new_row = []
            for row in matrix:
                new_row.append(row[r])
            res.append(new_row)
        return res