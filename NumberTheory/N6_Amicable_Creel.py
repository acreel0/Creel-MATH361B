# input variable
N = 300

# proper divisor function
def sum_prop_div(n):
    prop_div = []
    for i in range(1,int(n/2+1)):
        if n%i == 0:
            prop_div.append(i)
    sum_prop = sum(prop_div)
    return sum_prop

# create list for amicable numbers
amicable_numbers = []

# find amicable numbers
for a in range(1,N):
    d_a = sum_prop_div(a)
    for b in range(1,N):
        d_b = sum_prop_div(b)
        if d_a == b and d_b == a and a not in amicable_numbers:
            amicable_numbers.append(a)

print("The amicable numbers up to", N, "are:", amicable_numbers)