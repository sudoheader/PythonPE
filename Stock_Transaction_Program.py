# Last month Joe purchased some stock in Acme Software, Inc.
# Here are the details of the purchase:
# --The number of shares that Joe purchased was 1,000.
# --When Joe purchased the stock, he paid $32.87 per share.
# --Joe paid his stockbroker a commission that amounted to 2 percent of the
# amount he paid for the stock.
# Two weeks later Joe sold the stock. Here are the details of the sale:
# --The number of shares that Joe sold was 1,000.
# --He sold the stock for $33.92 per share.
# --He paid his stockbroker another commission that amounted to 2 percent of the
# amount he received for the stock.
#￼Write a program that displays the following information:
# --The amount of money Joe paid for the stock.
# --The amount of commission Joe paid his broker when he bought the stock.
# --The amount that Joe sold the stock for.
# --The amount of commission Joe paid his broker when he sold the stock.
# --Display the amount of money that Joe had left when he sold the stock and 
# paid his broker (both times). If this amount is positive, then Joe made a 
# profit.
# If the amount is negative, then Joe lost money.
purchasedShares = 1000
purchasedStock= 32.87
paidInCommission = 0.02
soldShares = 1000
soldStock = 33.92
receivedInCommission = 0.02
amountPaid = purchasedShares * purchasedStock
boughtCommission = paidInCommission * amountPaid
amountSold = soldShares * soldStock
soldCommission = receivedInCommission * amountSold
amountLeft = (amountPaid - amountSold) - (boughtCommission + soldCommission)
print('The amount of money Joe paid for the stock: $', \
	format(amountPaid, '.2f'), \
sep='')
print('The amount of commission Joe paid his broker when he bought the ', \
	'stock: $', \
	format(boughtCommission, '.2f'), \
sep='')
print('The amount that Joe sold the stock for: $', \
	format(amountSold, '.2f')
sep='')
print('The amount of commission Joe paid his broker when he sold the ', \
	'stock: $', \
	format(soldCommission, '.2f'), \
sep='')
print('The amount of money that Joe had when he sold the stock and paid ', \
	'his broker: $', \
	format(amountLeft, '.2f'), \
sep='')
