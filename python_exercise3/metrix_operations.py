def transpose(matrix):
    if not matrix or not matrix[0]:
        return [] 
    # Get dimensions
    rows = len(matrix)
    cols = len(matrix[0])
    # Create new matrix with swapped dimensions
    transposed = []
    for j in range(cols):           # for each original column
        new_row = []
        for i in range(rows):       # for each original row
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed
def matrix_sum(matrix):
    total = 0
    for row in matrix:
        for element in row:
            total += element
    return total
def row_with_max_sum(matrix):
    if not matrix:
        return -1
    max_sum = float('-inf')
    max_index = -1
    for i in range(len(matrix)):
        row_sum = 0
        for element in matrix[i]:
            row_sum += element
        
        if row_sum > max_sum:
            max_sum = row_sum
            max_index = i
    
    return max_index
# Sample matrix
matrix = [
    [1,  2,  3],
    [4,  5,  6],
    [7,  8,  9]
]

print("Original matrix:")
for row in matrix:
    print(row)

print("\nTranspose:")
for row in transpose(matrix):
    print(row)
# Output:
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]

print("\nSum of all elements:", matrix_sum(matrix))
# Output: 45

print("Row with maximum sum:", row_with_max_sum(matrix))
# Output: 2 (third row: 7+8+9 = 24)