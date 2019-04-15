
p = [1, 2, 3] # polynomial: 3x^2 + 2x + 1
c = 2
a = 1
b = 4

def evaluate(poly, c):
    pc = []
    for i in range(len(poly)):
        pp = poly[i]*(c**i) # mutiply the coefficient by c raised to the index(power)
        pc.append(pp) # append this value to the list
    return sum(pc) # return the sum of these values to give the result of the polynomial evaluated at c

def derive(poly, c):
    dpc = []
    for k in range(len(poly)):
        dpp = k*poly[k]*(c**(k-1)) # finds the product of the coefficent, power, and c raised to the power-1
        dpc.append(dpp) # appends this value to the list
    return sum(dpc) # returns the sum of these values to give the derivative of the polynomial evaluated at c

def integrate(poly, a, b):
    ipa = []
    ipb = []
    for m in range(len(poly)):
        pp1 = (poly[m]/(m+1))*(a**(m+1)) # finds the product of the coefficient, 1/power+1, and a raised to the power+1
        ipa.append(pp1) # appends this value to a list
        pp2 = (poly[m]/(m+1))*(b**(m+1)) # # finds the product of the coefficient, 1/power+1, and a raised to the power+1
        ipb.append(pp2) # appends this value to a list
    int_ab = sum(ipb)-sum(ipa) # subtracts the sum of the values in the "b" list and the sum of the values in the "a" list to evaluate the integral from a to b of the function
    return int_ab

epc = evaluate(p,c)
dpc = derive(p,c)
ip_ab = integrate(p,a,b)

print('p (', c, ') = ', epc)
print("p '(", c, ") = ", derive(p,2))
print('integral of p from', b, 'to', a, '=', integrate(p, 1, 4))