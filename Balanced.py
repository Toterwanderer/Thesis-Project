import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]])
all_nonzero = np.all(matrix != 0)
print(all_nonzero)

#We have a number of families stored locally - T
#We also have every subset of N, each S.
# We also have every

#Something like:
    
    #for each family in T #So family should store all S and all delta_S
        #Construct all Betas for that family
        #For each Beta
            #Sum delta_S P_S = Beta dot delta
            #We now have a perm matrix,X
            #Multiply perm matrix by depth (slight variation of BvN; fine)
            #initialize decomposition matrix, Dmat
            #for each P_n:
                #if X-P_n \ge 0 for all elements, we're cooking. 
                    #initialize a decomposition in Dmat, storing the matrix we subtracted.
                    #X=X-P_n
                    #While X-P_n \ge 0 for all elements:
                        #look through remaining P_n
                    #Close up decomposition k
                #else: continue #get next P_n. 
                
                
        #We want to associate EACH family with betas and their decompositions. 
        
        #Then, when we look at a new PI*, we just ask: what betas, P_n are allowed? Do any have a decomposition that is strong? If so: strong.
        #Do NONE have a decomposition that is weak? If so - SUCKS
        #Else: Weak
        