import math

#Time complexity: O(log(m×n))
#Space complexity O(1)
def searchMatrix(matrix, target):
    left = 0
    right = (len(matrix[0]) * len(matrix)) - 1 # Last index of the flat matrix

    while left <= right:
        index = left + (right - left) // 2 # Find the middle index
        r = index // len(matrix[0]) # Convert index to row number
        c = index % len(matrix[0]) # Convert index to column number

        if matrix[r][c] == target: # If the element is found
            return True
        elif matrix[r][c] < target: # If the element is smaller than the target
            left = index + 1
        else: # If the element is larger than the target
            right = index - 1

    return False

matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
target = 10

print(searchMatrix(matrix, target))

#Brute force
"""
def searchMatrix(matrix, target):
    for r in matrix:
        for c in r:
            if c == target:
                return True

    return False
"""

#O(n) solution
"""
def searchMatrix(matrix, target):
    result = []
    for r in matrix:
        result += r
    
    return target in result
"""