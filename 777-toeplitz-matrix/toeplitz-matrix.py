class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n-1):
            for j in range(m-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True
    # Time complexity: O(n∗m) - iterate through almost every element in the matrix once
    # Space complexity: O(1) - Only a few variables are used