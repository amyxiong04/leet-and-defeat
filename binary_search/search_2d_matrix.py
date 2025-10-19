class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # just treat it as a flattened 1D array tbh
        rows = len(matrix)
        cols = len(matrix[0]) 
        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            mid_row = mid // cols # this gives the row
            mid_col = mid % cols  # and this gives the column 

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False