import numpy as np

#Input Variables
N = 1000

terms_1 = np.array([])
new_term_1 = 1

terms_2 = np.array([])
new_term_2 = 1

terms_3 = np.array([])
new_term_3 = 1

#First Partial Product
for ii in range(2,N):
    new_term_1 = new_term_1*((ii**3 - 1)/(ii**3 + 1))
    terms_1 = np.append(terms_1,new_term_1)

#Second Partial Product
for nn in range(1,N):
    new_term_2 = new_term_2*(np.exp(nn/100)/(nn**10))
    terms_2 = np.append(terms_2,new_term_2)

#Third Partial Product
for ff in range(1,N):
    new_term_3 = new_term_3*(np.sin(ff)/(ff**2))
    terms_3 = np.append(terms_3,new_term_3)

#Print out the first 15 and last 15 terms of each product
seq = np.array([terms_1,terms_2,terms_3])
for zz in range(len(seq)):
    ww = zz + 1
    print("The first 15 terms of sequence", ww, "are: ")
    for xx in range(0,15):
        print(seq[zz][xx])
    print(" ")
    print("The last 15 terms of sequence", ww, "are: ")
    for yy in range(0,15):
        yy = yy - 16
        print(seq[zz][yy])
    print(" ")