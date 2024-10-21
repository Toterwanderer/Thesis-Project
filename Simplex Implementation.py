import numpy as np
import itertools
import time
from scipy.optimize import linprog

def filter_array(array, binary_number):
    # Ensure the binary number is a string of length 24
    binary_str = str(binary_number)

    # Create a mask based on the binary number
    mask = np.array([bit == '1' for bit in binary_str], dtype=bool)

    # Filter the array using the mask
    result = array[mask]

    return result

# Map each matrix to a letter, 24 unique 4x4 matrices
def string_to_matrix(s):
    # Initialize a 4x4 matrix of zeros
    matrix = np.zeros((4, 4), dtype=int)
    
    # Loop through each character in the input string
    for row, char in enumerate(s):
        matrix[row, int(char)-1] = 1
    
    return np.array(matrix)

# Construct matrix_map
matlib =[np.array(string_to_matrix(s)) for s in itertools.permutations('1234')]
letters = [chr(i) for i in range(ord('a'), ord('a') +len(matlib))]
matrix_map = dict(zip(letters,matlib))

# Example coefficient matrices (replace with your actual matrices)
#P = filter_array(np.array(matlib),'000000010110010011100011')
#hjkwsn
#P = filter_array(np.array(matlib),'000000010110010000100010')
#hqkwsn
P = filter_array(np.array(matlib),'000000010010010010100010')
BS = np.array([
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
])
flattened_BS = BS.flatten() 
flattened_P = [matrix.flatten() for matrix in P]
lin_constraints = np.column_stack(flattened_P)
print(lin_constraints)
print(flattened_BS)

# Objective coefficients (example, replace with your actual objective)
c = np.zeros(6)  # Objective function coefficients
print(c)

# # Combine all A matrices and b vectors
# A = np.vstack([A1, A2, A3, A4, A5, A6])
# b = np.concatenate([b1, b2, b3, b4, b5, b6])
# print(A)
# print(b)
# # Bounds for variables x
# x_bounds = [(0, 1) for _ in range(c.shape[0])]

 # Solve the linear programming problem
result = linprog(c, A_eq=lin_constraints, b_eq=flattened_BS, bounds=(0,1))
print(result.status)
#Check results
if result.success:
    print("Optimal value:", result.fun)
    print("Optimal solution:", result.x)
else:
      print("No solution found:", result.message)