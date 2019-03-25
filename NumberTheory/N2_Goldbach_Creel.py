import numpy as np

# Input Variables
N = 6000

# Prime check function

def prime_check(x):
    prime = True
    max_x = int(np.sqrt(x)+1)
    for ii in range(2,max_x):
        mod = x%ii
        if (mod != 0):
            prime = True
        elif (mod == 0):
            prime = False
            break
    return prime

# Create list of primes and composites

prime_list = [2]
composite_list = []
odd_composite = []

for kk in range(3,N):
    p = prime_check(kk)
    if p == True:
        prime_list.append(kk)
    else:
        composite_list.append(kk)

# Create list of odd composites
        
for ii in composite_list:
    if ii%2 != 0:
        odd_composite.append(ii)

# define Goldbach function

def Goldbach(g):
    G = False
    for pp in prime_list:
        for nn in range(500):
            right = pp + 2*(nn**2)
            if g == right:
                G = True
    return G

# test GB's other conjecture on odd composites
    
for jj in odd_composite:
    GB = Goldbach(jj)
    if GB == False:
        print("The smallest counterexample of Goldbach's other conjecture is", jj)
        break
    