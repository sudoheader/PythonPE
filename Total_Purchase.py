# A customer in a store is purchasing five items.
# Write a program that asks for the price of each item,
# and then displays the subtotal of the sale,
# the amount of sales tax, and the total.
# Assume the sales tax is 6 percent.
item1 = float(input('Enter the price of the first item:'))
item2 = float(input('Enter the price of the second item:'))
item3 = float(input('Enter the price of the third item:'))
item4 = float(input('Enter the price of the forth item:'))
item5 = float(input('Enter the price of the fifth tem:'))
subtotal = item1 + item2 + item3 + item4 + item5
sales_tax = 0.06
total_tax = subtotal * sales_tax
total = subtotal + total_tax
print('The subtotal of the sale is', sutotal)
print('The amount of the sale tax is', sales_tax)
print('The total is', total)
