# Input Variables
N = 20

f0 = 5
f1 = 8

fib_seq = [0] * N
cass_identity = []

# Fibonacci Sequence Generation
for ii in range(N):
    if ii == 0:
        fib_seq[0] = f0
    elif ii == 1:
        fib_seq[1] = f1
    else:
        fib_seq[ii] = fib_seq[ii-1] + fib_seq[ii-2]

print("The last 10 terms of this sequence are:", fib_seq[-10:])

# Check Cassini's Identity
for kk in range(1,N-1):
    cass1 = fib_seq[kk]**2 - (fib_seq[kk-1]*fib_seq[kk+1])
    cass2 = (-1)**(fib_seq[kk-1])
    if cass1 == cass2:
        cass_identity.append(True)
    else:
        cass_identity.append(False)
    print("cass 1 =", cass1, "and cass 2 =", cass2)
    diff = abs(cass1 - cass2)
    print("The difference between cass1 and cass2 is", diff)
    
print("The results of checking Cassini's identity are", cass_identity)
