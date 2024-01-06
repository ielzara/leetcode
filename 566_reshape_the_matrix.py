from typing import List

class Solution:
    def matrixReshape(mat, r, c):
    # Calculate the dimensions of the original matrix
        m, n = len(mat), len(mat[0])

    # Check if reshape is possible
        if m * n != r * c:
            return mat

    # Initialize the reshaped matrix with zeros
        reshaped = []
        for _ in range(r):
            row = []
            for _ in range(c):
                row.append(0)
            reshaped.append(row)

    # Iterate over the original matrix and fill the reshaped matrix
        row, col = 0, 0
        for i in range(m):
            for j in range(n):
                reshaped[row][col] = mat[i][j]
                col += 1
                if col == c:  # Move to the next row in the reshaped matrix
                    col = 0
                    row += 1

        return reshaped

# Example usage
print(matrixReshape([[1, 2], [3, 4]], 1, 4))  # Output: [[1, 2, 3, 4]]
print(matrixReshape([[1, 2], [3, 4]], 2, 4))  # Output: [[1, 2], [3, 4]]
