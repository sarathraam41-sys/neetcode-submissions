class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        current = 1
        for i in range(1, rowIndex + 1):
            current = current * (rowIndex - i + 1) // i
            row.append(current)
        return row
