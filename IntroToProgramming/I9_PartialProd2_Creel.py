import numpy as np

# Input Variables
N = 250

# Rational partial product:
f = lambda n: n**2
g = lambda n: n**5 + 6

a_n = lambda n: 1 + (f(n)/g(n))

seq = np.array([a_n(1)])

for ii in range(2,N):
    term = seq[-1] * a_n(ii)
    seq = np.append(seq, term)

print("The first 15 terms of the rational partial product sequence are", seq[:15])
print("The last 15 terms of the rational partial product sequence are", seq[-15:])

# Exponential partial product:
h = lambda n: 3**n

b_n = lambda n: 1 + h(n)

seq2 = np.array([b_n(1)])

for jj in range(2,N):
    term2 = seq2[-1] * b_n(jj)
    seq2 = np.append(seq2,term2)

print("The first 15 terms of the exponential partial product sequence are", seq2[:15])
print("The last 15 terms of the exponential partial product sequence are", seq2[-15:])