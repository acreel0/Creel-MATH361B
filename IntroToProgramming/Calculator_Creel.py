# Input Variables
x = 1
y = 3
z = 5

comp_1 = x + y
comp_2 = y*z + 3*x
comp_3 = comp_1**2
comp_4 = (2*comp_2 - (1/2)*x)/comp_1
comp_5 = 7%3

my_list = [comp_1, comp_2, comp_3, comp_4, comp_5]

my_list[2] = comp_3 + 3

my_list[-1] = comp_5*(3/4)

sum_of_list = sum(my_list)
length = len(my_list)

print("There are", length, "components in the list, and sum of these", length, "components is", sum_of_list)