'''
THIS CODE PROVIDES A WAY OF RELIABLY DECOMPOSING A GIVEN MATRIX USING BIRKHOFF
ALGORITHM. 

SOME TODOS:
    -Would like to get a ready list of all matrices included in decompositions
    -Perhaps optimize code by doing this before a function call? i.e.: narrow down our list first thing, then proceed.
    -See if we have any clear patterns by iterating this over a wide spread.
    -See if a couple combo of 6 permutations in a given I-P can generate a solution using simplex
        (as simplex would definitely yield one IF it existed.)
        If we are thinking '6 unimportant', '5 unimportant, 1 impo' , '4 unimpo, 2 impo'
        OKAY, so actually, all 6'unimportant' is enough to get a decomposition. 
        This is a linear combination of the other decompositions, in a sense. If you add 3, then take away one, 
        we get this one
TIMING: 
    Each decomposition takes between 1/250 and 1/500 of a second. 
    For a given PI*, we have 11 families to test of 3 classes.
        1 class: 6^4 = 1296 at most, 1 at min.
        2 class(4): 2*2*2*6 =48 at most, 1 at min.
        3 class(6): 2*6^2 = 72 at most, 1 at min
        So we have between 1 and 1920. Probably about 200 on average.
        So that's each PI* taking 1 second.Call that 12 days computation.
TAKEAWAYS:
    Each of our decompositions of I-P (P permutation), which we expect to be a reasonably large set
    has 4 decompositions, each consisting of 3 elements, 9 total permutations that 'fit inside'
    
        This makes sense: If we have I-P = a+b+c, then we get a different I-P by multiplying by a permutation matrix:
            We permute the locations of the 0s. So we can think of each of these permutation matrices as being
            part of the same equivalence class, and similarly, the structure of our decompositions are also
            permutations times our original decompositions. SO, all of them of the same "shape" have the same
            decomposition structure. Cool linear algebra.
    The 3,3,3,3 matrices all have one decomposition: 3P, where P is a perm matrix
    The '2x2x2' matrices all have one decomposition. ONLY 3 elements fit inside, and each decomposition requires 
        at least 3 elements, as some row/column has 3 distinct entries nonzero, meaning every decomposition
        is exactly those elements. 
    WOW the casework is tedious Q_Q
'''
    


import numpy as np
import itertools
import time

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


# Function to decompose BS and return letter representations or binary strings
def decompose(BS, allmat, start=0, decomp=None, index_included=None):
    # Initialize decomposition and index tracking if not provided
    if decomp is None:
        decomp = []
    if index_included is None:
        index_included = []
    
    # TESTING: Print current state of BS and the depth of recursion
    #print(f"Current BS:\n{BS}\nDepth: {len(decomp)}")
    
    # Base case: If BS reaches all zeros, return the current decomposition as a string or binary number
    if np.all(BS == 0):
        # Return as letters ('ADE') or binary string ('100110')
        letters_included = ''.join([letters[i] for i in index_included])
        #IF WE WANT BINARY: 
        #binary_included = ''.join(['1' if i in index_included else '0' for i in range(len(allmat))])
        #IF WE WANT COUNTS: 
        binary_included = ''.join([str(index_included.count(i)) if i in index_included else '0' for i in range(len(allmat))])
        return [(letters_included, binary_included)]
    
    # Store all valid decompositions
    results = []
    
    # Recursive case: iterate through the allowable matrices
    for i in range(start, len(allmat)):
        M = allmat[i]
        # Skip this matrix if subtracting it results in negative values
        if np.any(BS - M < 0):
            continue
        
        # Recur with the reduced BS, updated decomposition, and updated index list
        result = decompose(BS - M, allmat, i, decomp + [M], index_included + [i])
        
        # If a valid decomposition is found, add it to the results
        if result:
            results.extend(result)
    
    return results if results else []

def empty_decomposition(BS,allmat):
    results = decompose(BS,allmat)
    if results:
        for letters_included, binary_included in results:
            print(f"Letters: {letters_included}, Binary: {binary_included}")
        return results
    else: print("No decompositions exist for the given matrix")

# Define a target 4x4 matrix BS
BS = np.array([
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
])

# Run decomposition and print the results
start=time.time()
hmm = empty_decomposition(BS,matlib)
print(time.time()-start)

print('h:',matrix_map['h'],'\nq:',matrix_map['q'],'\nx:',matrix_map['x'])
print('r:',matrix_map['r'],'\nj:',matrix_map['j'],'\nk:',matrix_map['k'])
print('w:',matrix_map['w'],'\ns:',matrix_map['s'],'\nn:',matrix_map['n'])

# #Some easy test decompositions
# for key in matrix_map:
#     start = time.time()
#     BS = matrix_map[key]
#     BS = np.ones([4,4])-BS
#     print(key)
#     empty_decomposition(BS, matlib)
#     print(time.time()-start)

#2/3 matrix structure
# BS = np.array([
#     [0, 2, 0, 1],
#     [0, 0, 2, 1],
#     [2, 0, 0, 1],
#     [1, 1, 1, 0]
# ])
# start=time.time()
# empty_decomposition(1*BS,matlib)
# print(time.time()-start)
# for key in matrix_map:
#     start = time.time()
#     B = np.matmul(BS,matrix_map[key])
#     print(B)
#     print(key)
#     empty_decomposition(B,matlib)
#     #print(time.time()-start)


    