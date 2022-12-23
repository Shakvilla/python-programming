# Write a function that computes the square value of all integers of a matrix.
#
# Prototype: def square_matrix_simple(matrix=[]):
# matrix is a 2 dimensional array
# Returns a new matrix:
# Same size as matrix
# Each value should be the square of the value of the input
# Initial matrix should not be modified
# You are not allowed to import any module
# You are allowed to use regular loops, map, etc.

# ***********************PSEUDOCODE*******************
# make a copy of the matrix and work with that
# Take an integer from the matrix
# Multiply the integer by itself and print the result
# Move to the next integer and perform the same operation

def square_matrix_simple(matrix=[]):
    copied_matrix = matrix.copy()

