import numpy as np

# input variables
# P = maximum value for p
P = 55

x = np.zeros([0,2])

def prime_check(x):
    prime = True
    for ii in range(2,x):
        mod = x%ii
        if (mod != 0):
            prime = True
        elif (mod == 0):
            prime = False
            break
    return prime

primes_P = []

for ii in range(1,P):
    prime = prime_check(ii)
    if prime == True:
        primes_P.append(ii)

for p in primes_P:
    quad_res = [0]
    for n in range(p):
        for kk in range(p):
            if (kk**2)%p == n and n not in quad_res:
                quad_res.append(n)
    x = np.vstack([x, np.array([p, len(quad_res)])])

print('The number of quadratic residues in Zp are:')
print(x)

neg_one = np.zeros([0,2])

for pp in primes_P:
    for nn in range(pp):
        neg1 = False
        if (nn**2)%pp == (pp-1):
            neg1 = True
            neg_one = np.vstack([neg_one, np.array([pp, 'yes'])])
            break
    if neg1 == False:
        neg_one = np.vstack([neg_one, np.array([pp, 'no'])])

print('Is -1 a quadratic residue in Zp?')
print(neg_one)
  