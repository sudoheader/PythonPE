# A company has determined that its annual profit is typically 
# 23 percent of total sales. Write a program that asks the user 
# to enter the projected amount of total sales, and then displays 
# the profit that will be made from that amount.
annual_profit = 0.23
total_sales = input('Enter the projected amount of total sales: ')
profit = float(annual_profit * total_sales)
print('The profit that will be made from the total sales is', \
	profit)
