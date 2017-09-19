# Write a program that will ask the user to enter
# the amount of a purchase. The program should then
# compute the state and county sales tax. 
# Assume the state sales tax is 4 percent and the
# county sales tax is 2 percent. The program should
# display the amount of the purchase, the state
# sales tax, the county sales tax, the total sales
# tax, and the total of the sale (which is the sum
# of the amount of purchase plus the total sales tax).
amount = float(input('Enter the amount of the purchase: ')) 
state_tax = 0.04
county_tax = 0.02
total_tax = state_tax + county_tax
total_sale = amount * total_tax
sale = amount + total_sale
print('The amount of the purchase is', amount)
print('The state sales tax is', state_tax)
print('The county sales tax is', county_tax)
print('The total sales tax is', total_tax)
print('The total of the sale is', sale)
