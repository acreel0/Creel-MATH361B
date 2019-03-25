
# input variable
m = 7

# list to store the multiplicative inverses in
mult_inv = []

# for loop to find multiplicative inverses and add them to the list
for i in range(2,m-1):
    for j in range(2,m-1):
        k = (i*j)%m
        if k == 1 and i not in mult_inv:
            mult_inv.append(i)
            mult_inv.append(j)

print("The elements which have a multiplicative inverse are", mult_inv, ". There are", len(mult_inv), "elements with a multiplicative inverse.")
