class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        cols = len(matrix[0])
        for i in range(row):
            for j in range(cols):
                if matrix[i][j]==target:
                    return True
                    break
        return False        