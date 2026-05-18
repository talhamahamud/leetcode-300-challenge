class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        # Hash sets to store the indices of rows and columns that should be zeroed
        zero_rows = set()
        zero_cols = set()
        
        # Step 1: First pass to find all original zeros
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)
                    
        # Step 2: Second pass to update the matrix in-place
        for r in range(m):
            for c in range(n):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0