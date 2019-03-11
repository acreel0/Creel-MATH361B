
def collatz(a0,N):
   # a0 = initial term
   # N = total number of terms to compute
    coll_list=[a0]
    
    for ii in range(N):
        
        if (coll_list[ii]%2 == 0):
            term = coll_list[-1]/2
            
        else:
            term = 3*coll_list[-1]+1
            
        coll_list.append(term)
        
        if (term == 1):
            return coll_list
        
    return coll_list

# Input Variables
a0 = 27
N = 40

seq = collatz(a0,N)

print("The sequence is", seq)

if len(seq)< N:
    print("It took", len(seq), "terms to reach 1.")
    
else:
    print("After", N, "terms, we did not reach 1.")