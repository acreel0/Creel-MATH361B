# Defining Collatz Function
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
a0 = 6**3
N = 200

seq = collatz(a0,N)

print("The sequence is", seq)

if len(seq)< N:
    print("It took", len(seq), "terms to reach 1.")
    
else:
    print("After", N, "terms, we did not reach 1.")

M = len(seq)
even = []
odd = []
for kk in range(M):
    if seq[kk]%2 == 0:
        even.append(seq[kk])
    else:
        odd.append(seq[kk])

percent_even = (len(even)/len(seq))*100
percent_odd = (len(odd)/len(seq))*100
print("There are ", len(even), "even terms in the sequence and", len(odd), "odd terms in the sequence. Even terms make up", percent_even, "percent of the sequence, and odd terms make up", percent_odd, "percent of the sequence.")


# look at powers of three (even powers of three and odd powers of three)
# start with 3 -- 8 terms
# start with 6 -- 9 terms
# start with 9 -- 20 terms
# start with 12 -- 10 terms
# start with 15 -- 18 terms
# start with 21 -- 8 terms
# start with 27 -- 112 terms
# start with 33 -- 27 terms
# start with 39 -- 35 terms

# a power of 2 will eventually reach 2
# 2 took 2 terms
# 4 took 3 terms
# 8 took 4 terms
# 16 took 5 terms
# 32 took 6 terms

# CONJECTURE NUMBER ONE:  
# 2 ^ n will have n+1 terms in the sequence after reaching one (converging)
# e.g., 2^1 = 2 -- 2 terms
# e.g., 2^2 = 4 -- 3 terms

# prime numbers
    # 3 took 8
    # 7 took 17
    # 11 took 15
    # 13 took 10
    # 17 took 13
    # 19 took 21
    # 23 took 16

# powers of 10
    # 10 took 7
    # 100 took 26
    # 1000 took 112
    # 10000 took 30

# CONJECTURE NUMBER TWO:
# powers of three will reach 16 and then start to converge because 16 is a power of 2
    # 3 - 16
    # 9 - 16
    # 27 - 16
    # 81 - 16

# CONJECTURE NUMBER TWO.5:
    # powers of 5 will reach 16 then start to converge because 16 is a power of 2

# powers of 2k+1 will reach 16 then converge because 16 is a power of 2
    
# 4 starts converging at 4
# 9 starts converging at 16
# 16 starts at 16
# 25 starts at 16

# CONJECTURE THREE: For powers of three, at least 60% of the terms will be even, and at most 40% of the terms will be odd.
# powers of three:
    # 3 -- 62.5% even, 37.5% odd
    # 9 -- 65% even, 35% odd
    # 27 --62.5% even, 37.5% odd
    # 81 -- ~69.5% even, ~30.5% odd
    # 243 -- ~64% even, ~ 36% odd
    # powers of 3 -- about twice as many even numbers as odd numbers in the sequence
    # 729 -- ~ 70.6% even, ~ 29.4% odd
    # 2187 -- ~ 66% even, ~33% odd
# look at prime powers vs. composite powers
# powers of five:
    # 5 -- ~ 66.6% even, ~33.3% odd
    # 25 -- ~ 66.6% even, ~ 33.3% odd
    # 125 -- ~ 63.3% even, ~ 36.7% odd
# powers of six:
    # 6 -- ~66.6% even, ~33.3% odd
    # 36 -- ~68% even, ~ 32% odd
# excluding powers of two, starting the sequence with a power of any integer (ex. 3^ of something)
    # will give at least 60% evens