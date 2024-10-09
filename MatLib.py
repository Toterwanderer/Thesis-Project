import numpy as np
#PI_star has all of my simple permutations

#This generates a binary string of the 24 possible matrices in PI*N - the allowable N permutations
def n_perms(p_str):
    p_str = str(p_str)
    if len(p_str) != 20:
        raise ValueError("Input must be a twenty-digit number.")
    if p_str[0]+p_str[5]=='11': p_str = p_str+'1'
    else:p_str = p_str+'0'
    if p_str[1]+p_str[4]=='11': p_str = p_str+'1'
    else:p_str = p_str+'0'
    if p_str[2]+p_str[3]=='11': p_str = p_str+'1'
    else:p_str = p_str+'0'
    p_str = '1'+p_str #place 1 in front, as I is always a fine permutation.
    return p_str
#a = '10111011100010000100'
#print("PI*:  ",a)
#print("PI*N:",n_perms(a))

#This filters PIN above by the binary string.
def filter_array(array, binary_number):
    # Ensure the binary number is a string of length 24
    binary_str = str(binary_number)

    # Create a mask based on the binary number
    mask = np.array([bit == '1' for bit in binary_str], dtype=bool)

    # Filter the array using the mask
    result = array[mask]

    return result

#Example using PIN
#print('only odd entries of PIN:\n',filter_array(PI_N,101010101010101010101010))

#Composite example using a given PI*
#PI_ = 10110100001001001001
#print('PI*:  ', PI_)
#print('PI*N:', n_perms(PI_))
#print('allowable n-permutations:\n',filter_array(PI_N,n_perms(10110100001001001001)))
#print(PI_star)


def unique_matrices(matrix_list):
    """
    "Filters duplicates out, counting unique entries"

    Parameters
    ----------
    matrix_list : a list of matrices

    Returns
    -------
    Unique matrices, 
    count of each occurence in matrix_list
    duplicate_matrices.

    """
    unique_matrices = []
    counts = []
    duplicate_matrices = []
    for matrix in matrix_list:
        is_unique = True
        for index, unique_matrix in enumerate(unique_matrices):
            if np.array_equal(matrix, unique_matrix):
                duplicate_matrices.append(matrix)
                is_unique = False
                counts[index] +=1
                break
        if is_unique:
            unique_matrices.append(matrix)
            counts.append(1)
    return unique_matrices, counts, duplicate_matrices

# Example usage
matrices = [
    np.array([[1, 2], [3, 4]]),
    np.array([[1, 2], [3, 4]]),
    np.array([[5, 6], [7, 8]])
]
matrices = [
    np.array([1, 2]),np.array([3, 4]),
    np.array([3, 4]), np.array([3, 4]), np.array([3, 4]),
    np.array([1, 2]), np.array([1, 2]),
    np.array([5, 6])
]
A,B,C = unique_matrices(matrices)
A =np.array(A)
B = np.array(B)

#print(A)
#print(B)
#print(C)

#Nice Matrix Libraries
PI_star = [
#12
np.array(
[[0, 1, 0, 0],
 [1, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]]),
#13
np.array(
[[0, 0, 1, 0],
 [0, 0, 0, 0],
 [1, 0, 0, 0],
 [0, 0, 0, 0]]),
#14
np.array(
[[0, 0, 0, 1],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [1, 0, 0, 0]]),
#23
np.array(
[[0, 0, 0, 0],
 [0, 0, 1, 0],
 [0, 1, 0, 0],
 [0, 0, 0, 0]]),
#24
np.array(
[[0, 0, 0, 0],
 [0, 0, 0, 1],
 [0, 0, 0, 0],
 [0, 1, 0, 0]]),
#34
np.array(
[[0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 1],
 [0, 0, 1, 0]]),
#123
np.array(
[[0, 1, 0, 0],
 [0, 0, 1, 0],
 [1, 0, 0, 0],
 [0, 0, 0, 0]]),
#132
np.array(
[[0, 0, 1, 0],
 [1, 0, 0, 0],
 [0, 1, 0, 0],
 [0, 0, 0, 0]]),
#124
np.array(
[[0, 1, 0, 0],
 [0, 0, 0, 1],
 [0, 0, 0, 0],
 [1, 0, 0, 0]]),
#142
np.array(
[[0, 0, 0, 1],
 [1, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 1, 0, 0]]),
#134
np.array(
[[0, 0, 1, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 1],
 [1, 0, 0, 0]]),
#143
np.array(
[[0, 0, 0, 1],
 [0, 0, 0, 0],
 [1, 0, 0, 0],
 [0, 0, 1, 0]]),
#234
np.array(
[[0, 0, 0, 0],
 [0, 0, 1, 0],
 [0, 0, 0, 1],
 [0, 1, 0, 0]]),
#243
np.array(
[[0, 0, 0, 0],
 [0, 0, 0, 1],
 [0, 1, 0, 0],
 [0, 0, 1, 0]]),
#1234
np.array(
[[0, 1, 0, 0],
 [0, 0, 1, 0],
 [0, 0, 0, 1],
 [1, 0, 0, 0]]),
#1243
np.array(
[[0, 1, 0, 0],
 [0, 0, 0, 1],
 [1, 0, 0, 0],
 [0, 0, 1, 0]]),
#1324
np.array(
[[0, 0, 1, 0],
 [0, 0, 0, 1],
 [0, 1, 0, 0],
 [1, 0, 0, 0]]),
#1342
np.array(
[[0, 0, 1, 0],
 [1, 0, 0, 0],
 [0, 0, 0, 1],
 [0, 1, 0, 0]]),
#1423
np.array(
[[0, 0, 0, 1],
 [0, 0, 1, 0],
 [1, 0, 0, 0],
 [0, 1, 0, 0]]),
#1432
np.array(
[[0, 0, 0, 1],
 [1, 0, 0, 0],
 [0, 1, 0, 0],
 [0, 0, 1, 0]]),
]

#PI_N has all N permutations
PI_N = [
#I
np.array(
[[1, 0, 0, 0],
 [0, 1, 0, 0],
 [0, 0, 1, 0],
 [0, 0, 0, 1]]),
#12
np.array(
[[0, 1, 0, 0],
 [1, 0, 0, 0],
 [0, 0, 1, 0],
 [0, 0, 0, 1]]),
#13
np.array(
[[0, 0, 1, 0],
 [0, 1, 0, 0],
 [1, 0, 0, 0],
 [0, 0, 0, 1]]),
#14
np.array(
[[0, 0, 0, 1],
 [0, 1, 0, 0],
 [0, 0, 1, 0],
 [1, 0, 0, 0]]),
#23
np.array(
[[1, 0, 0, 0],
 [0, 0, 1, 0],
 [0, 1, 0, 0],
 [0, 0, 0, 1]]),
#24
np.array(
[[1, 0, 0, 0],
 [0, 0, 0, 1],
 [0, 0, 1, 0],
 [0, 1, 0, 0]]),
#34
np.array(
[[1, 0, 0, 0],
 [0, 1, 0, 0],
 [0, 0, 0, 1],
 [0, 0, 1, 0]]),
#123
np.array(
[[0, 1, 0, 0],
 [0, 0, 1, 0],
 [1, 0, 0, 0],
 [0, 0, 0, 1]]),
#132
np.array(
[[0, 0, 1, 0],
 [1, 0, 0, 0],
 [0, 1, 0, 0],
 [0, 0, 0, 1]]),
#124
np.array(
[[0, 1, 0, 0],
 [0, 0, 0, 1],
 [0, 0, 1, 0],
 [1, 0, 0, 0]]),
#142
np.array(
[[0, 0, 0, 1],
 [1, 0, 0, 0],
 [0, 0, 1, 0],
 [0, 1, 0, 0]]),
#134
np.array(
[[0, 0, 1, 0],
 [0, 1, 0, 0],
 [0, 0, 0, 1],
 [1, 0, 0, 0]]),
#143
np.array(
[[0, 0, 0, 1],
 [0, 1, 0, 0],
 [1, 0, 0, 0],
 [0, 0, 1, 0]]),
#234
np.array(
[[1, 0, 0, 0],
 [0, 0, 1, 0],
 [0, 0, 0, 1],
 [0, 1, 0, 0]]),
#243
np.array(
[[1, 0, 0, 0],
 [0, 0, 0, 1],
 [0, 1, 0, 0],
 [0, 0, 1, 0]]),
#1234
np.array(
[[0, 1, 0, 0],
 [0, 0, 1, 0],
 [0, 0, 0, 1],
 [1, 0, 0, 0]]),
#1243
np.array(
[[0, 1, 0, 0],
 [0, 0, 0, 1],
 [1, 0, 0, 0],
 [0, 0, 1, 0]]),
#1324
np.array(
[[0, 0, 1, 0],
 [0, 0, 0, 1],
 [0, 1, 0, 0],
 [1, 0, 0, 0]]),
#1342
np.array(
[[0, 0, 1, 0],
 [1, 0, 0, 0],
 [0, 0, 0, 1],
 [0, 1, 0, 0]]),
#1423
np.array(
[[0, 0, 0, 1],
 [0, 0, 1, 0],
 [1, 0, 0, 0],
 [0, 1, 0, 0]]),
#1432
np.array(
[[0, 0, 0, 1],
 [1, 0, 0, 0],
 [0, 1, 0, 0],
 [0, 0, 1, 0]]),
#12,34
np.array(
[[0, 1, 0, 0],
 [1, 0, 0, 0],
 [0, 0, 0, 1],
 [0, 0, 1, 0]]),
#13,24
np.array(
[[0, 0, 1, 0],
 [0, 0, 0, 1],
 [1, 0, 0, 0],
 [0, 1, 0, 0]]),
#14,23
np.array(
[[0, 0, 0, 1],
 [0, 0, 1, 0],
 [0, 1, 0, 0],
 [1, 0, 0, 0]]),
]
PI_star = np.array(PI_star)
PI_N = np.array(PI_N) #necessary for later work.