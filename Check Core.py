from MatLib import PI_star,PI_N,filter_array,n_perms
import itertools
import numpy as np
import time
import random
start=time.time()

#PI_ = '11010000000000000000' #3 player roommates
#PI_ = '11111111111111111111' #Everything allowed.
#PI_ = '00000000000000000000'
PI_ = '11111100000000000000'
#PI_ = ''.join(random.choice('01') for _ in range(20)) #make random PI*
preferences = list(itertools.permutations(range(1,5))) #make a permanent list

def modify_nested_list(nested_list, target):
    new_list = []
    
    for sublist in nested_list:
        modified_sublist = list(sublist)  # Convert tuple to list if necessary
        key = modified_sublist[target-1] #How do we rank our house?
        for index, element in enumerate(modified_sublist):
            if element > key: #If we like it less, we'll NEVER use it.
                modified_sublist[index] = 5
        new_list.append(tuple(modified_sublist))

    return list(dict.fromkeys(new_list))

print("PI*: ", PI_)
#print(n_perms(PI_))
PI = filter_array(PI_star,PI_)
PIN = filter_array(PI_N,n_perms(PI_))
#print(PI, "then PIN", PIN)
#print("\nAllowable Simple Permutations:\n",PI)
#print("\n Allowable N Permutations:",PIN)
modify_nested_list(preferences,1)
break1=0
for r1 in modify_nested_list(preferences,1): #R1
    for r2 in modify_nested_list(preferences,2): #R2
        for r3 in modify_nested_list(preferences,3): #R3
            for r4 in modify_nested_list(preferences,4): #R4 and step 2
                #r1,r2,r3,r4= [(3,1,2,4),(2,3,1,4),(1,2,3,4),(2,3,4,1)] 
                #print('r1:',r1,'\nr2:',r2,'\nr3:',r3,'\nr4:',r4)
                break2=0
                for Pn in PIN: #step 3
                    break3 = 0
                    for Ps in PI: #step 4
                        break4 = 0
                        indicator = 0
                        #We build a reference matrix from matrix multiplication.
                        Psr = np.array([np.dot(Ps,r1)[0],np.dot(Ps,r2)[1],np.dot(Ps,r3)[2],np.dot(Ps,r4)[3]])
                        Pnr = np.array([np.dot(Pn,r1)[0],np.dot(Pn,r2)[1],np.dot(Pn,r3)[2],np.dot(Pn,r4)[3]])
                        #print('Ps:\n',Ps,'\nPn:\n',Pn)
                        #print('Psr:',Psr,'\nPnr:',Pnr)
                        for i in range(1,5):
                            if np.sum(Ps,axis=1)[i-1] == 0: #if row sum equals 0 // if trader i isn't in the coalition S, we move on. 
                                #print("WHO CARES>_>")
                                continue #get next i and restart for loop
                            elif Psr[i-1] == Pnr[i-1]:
                                #print("EQUAL")
                                continue #get next i
                            elif Psr[i-1] < Pnr[i-1]:
                                #print("LESS")
                                indicator = 1
                                continue #get next i
                            else:
                                #print("MORE")
                                break4 = True
                                break
                        if break4 == 1:
                            continue #get next Ps 
                        else:
                            if indicator == 0:
                                continue #get next Ps
                            if indicator == 1:
                                #print("HALLELUJAH?")
                                break3 = 1
                                break #go to step 3
                    if break3 ==1:
                        #print("Some Ps blocks")
                        continue #get next Pn / go to step 3
                    else: 
                        #print("No Ps blocks")
                        break2 = 1
                        break
                if break2 ==1:
                    #print("Good sign: We have a core for this set of preferences")
                    continue
                else:
                    #print("This set of preferences has no core")
                    print("PI* DOES NOT HAVE NONEMPTY STRICT CORE PROPERTY")
                    print('r1:',r1,'\nr2:',r2,'\nr3:',r3,'\nr4:',r4)
                    break1 = 1
                    break
            if break1==1:
                break
        if break1==1:
                break
    if break1==1:
                break
#   continue #get next preference
#break
if break1==0:
    print("PI* HAS NONEMPTY STRICT CORE PROPERTY")
#How do we know, after finishing up all P_ns, if we're done or not? If a single P_s blocks, we want the next P_n. 
#If NO P_s blocks, we're like, great, this the P_n, and we get the next

print("TIME: ", time.time()-start)