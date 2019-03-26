# proper divisor function
def prop_div(n):
    prop_list = []
    for i in range(1,n-1):
        if n%i == 0:
            prop_list.append(i)
    return prop_list

# input variable
m = 10

print("The proper divisors of", m, "are", prop_div(m))