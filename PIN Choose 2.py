#All balanced 2 decompositions
from MatLib import PI_star,PI_N,filter_array,n_perms, unique_matrices
import numpy as np
from itertools import combinations

PI_N_C2= [mat1+mat2 for mat1, mat2 in combinations(PI_N,2)]
PI_N_C2=np.array(PI_N_C2)

print("How many do we have~~",len(PI_N_C2))
A,B,C = unique_matrices(PI_N_C2)

print(len(A))
print(np.array(C))

