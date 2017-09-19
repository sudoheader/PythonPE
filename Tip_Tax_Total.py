# Write a program that calculates the total amount of a meal purchased at a
# restaurant. The program should ask the user to enter the charge for the food, # and then calculate the amount of a 15 percent tip and 7 percent sales tax.
# Display each of these amounts and the total.
charge = float(input('Enter the charge for the food:')
tip = 0.15
sales_tax = 0.07
total = charge * (tip + sales_tax)
total_amount = charge + total
print('The charge of the meal is', charge)
print('The tip is set at 15 percent')
print('The sales tax is set at 7 percent')
print('The total amout of the meal is', total_amount)
