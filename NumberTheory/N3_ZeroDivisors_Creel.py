# input variables
m = 12

# create a list for zero divisors
zero_div = []

# for loop to find zero divisors and add them to the list
for i in range(1,m):
    if m%i == 0 and i not in zero_div:
        zero_div.append(i)
        j = int(m/i)
        zero_div.append(j)

print("The zero divisors are", zero_div, ". There are", len(zero_div), "zero divisors.")