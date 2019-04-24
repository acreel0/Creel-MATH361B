import numpy as np

def clean_poly(p):
    highest_deg = len(p) - 1   
    for ii in range(len(p)-1,-1,-1):
        if np.abs(p[ii]) > 1e-15:
            break
        else:
            highest_deg -= 1
    del p[highest_deg+1:]
    return p

def add(p1, p2):
    if len(p1)>len(p2):
        added = list(p1)
        for i in range(len(p2)):
            added[i] = p1[i]+p2[i]
    else:
        added = list(p2)
        for j in range(len(p1)):
            added[j] = p1[j]+p2[j]
    return added

def subtract(p1, p2):
    if len(p1)>len(p2):
        subtracted = list(p1)
        for i in range(len(p2)):
            subtracted[i] = p1[i] - p2[i]
    else:
        subtracted = [0]*len(p2)
        for j in range(len(p1)):
            subtracted[j] = p1[j] - p2[j]
        for k in range (len(p1),len(p2)):
            subtracted[k] = 0 - p2[k]
    clean_poly(subtracted)
    return subtracted

def multiply(p1, ratio):
    multiplied = [0]*(len(p1)+len(ratio)-1)
    LT = ratio[-1]
    for i in range(len(p1)):
        ind = i+len(ratio)-1
        multiplied[ind] = LT*p1[i]
    return multiplied

def ratio(p1, p2):
    M = len(p1)-len(p2)
    ratio = [0]*(M+1)
    ratio[-1] = p1[-1]/p2[-1]
    return ratio

def poly_div(f,g):
    q = [0]
    r = f
    while r!=[0] and len(g)<=len(r):
        LT = ratio(r,g)
        q = add(q,LT)
        rLT = multiply(g,LT)
        r = subtract(r,rLT)
    return q, r

# test 1:
f = [7, 6, 0, 3]
# 3x^3 + 6x + 7
g = [3, 2]
# 2x + 3
q, r = poly_div(f,g)
print('f:',f)
print('g:',g)
print('Polynomial division of f/g results in:')
print('quotient q:',q)
print('remainder r:',r)

# test 2:
ff = [9,2,7,2]
# 2x^3 + 7x^2 + 2x + 9
gg = [3,2]
# 2x + 3
qq, rr = poly_div(ff,gg)
print('f:',ff)
print('g:',gg)
print('Polynomial division of f/g results in:')
print('quotient q:',qq)
print('remainder r:',rr)