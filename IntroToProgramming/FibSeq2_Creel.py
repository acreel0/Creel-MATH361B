# Input Variables
N = 100000
m = 2

f0 = 0
f1 = 1

fib_seq = [0] * N
multiples_m = []
index_multiples = []

# Fibonacci Sequence Generation
for ii in range(N):
    if ii == 0:
        fib_seq[0] = f0
    elif ii == 1:
        fib_seq[1] = f1
    else:
        fib_seq[ii] = fib_seq[ii-1] + fib_seq[ii-2]

# Checking multiples of m
for kk in range(N):
    if fib_seq[kk] % m == 0:
        multiples_m.append(fib_seq[kk])
        index_multiples.append(kk)

percent_m = (len(multiples_m))/(len(fib_seq)) * 100

print("There are", len(multiples_m), "multiples of", m, "in the first", N, "terms of the Fibonacci Sequence")
#print("The terms that are divisible by", m,  "are", multiples_m)
#print("The percentage of the first", N, "terms that are multiples of", m, "is", percent_m, "percent")
#print("The indexes of these terms are", index_multiples)