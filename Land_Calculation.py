# One acre of land is equivalent to 43,560 square feet.
# Write a program that asks the user to enter the total
# square feet in a tract of land and calculates the number
# of acres in the tract.
total_sqft = float(input('Enter the total square feet', \
	'in the tract of land'))
num_of_acres = total_sqft / 43560
print('The number of acres is', num_of_acres)
