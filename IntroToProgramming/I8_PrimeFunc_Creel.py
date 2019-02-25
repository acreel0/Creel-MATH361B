# import numpy as np
# Input variables
N=11

def prime_check(x):
    prime = True
    # max = int(np.sqrt(x))
    for ii in range(2,x):
        mod = x%ii
        if (mod != 0):
            prime = True
        elif (mod == 0):
            prime = False
            break
    return prime

prime_list = [2]
for kk in range(3,10000):
    primality = prime_check(kk)
    if (primality == True):
        prime_list.append(kk)
        if (len(prime_list) == N):
            break

n = str(N)

if (N >= 11 and N<=13):
    print("the", N, "th prime number is", prime_list[-1])
elif (int(n[-1])==1):
    print ("the", N, "st prime number is", prime_list[-1])
elif (int(n[-1])==2):
    print("the", N, "nd prime number is", prime_list[-1])
elif (int(n[-1])==3):
    print("the", N, "rd prime number is", prime_list[-1])
else:
    print("the", N, "th prime number is", prime_list[-1])