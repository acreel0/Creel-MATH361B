
# input variable
m = 24

# list to store the multiplicative inverses in
mult_inv = []

# for loop to find multiplicative inverses and add them to the list
for i in range(1,m):
    for j in range(1,m):
        k = (i*j)%m
        if k == 1 and i not in mult_inv:
            mult_inv.append(i)

#print("The elements which have a multiplicative inverse are", mult_inv, ". There are", len(mult_inv), "elements with a multiplicative inverse.")
print(m, ":", mult_inv)

# 10 : [1, 3, 7, 9]
# 12 : [1, 5, 7, 11]
# 15 : [1, 2, 4, 7, 8, 11, 13, 14]
    # 3, 5, 9, 10, 12
# 18 : [1, 5, 7, 11, 13, 17]
# 25 : [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24]

# numbers that aren't multiples of m
# the greatest common divisor of m and an inverse in m is 1
    # 10 and 1 -- 1, 10 and 3 -- 1, 10 and 7 -- 1