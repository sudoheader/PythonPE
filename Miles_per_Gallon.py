# A car’s miles-per-gallon (MPG) can be calculated with the following formula:
# MPG = Miles driven / Gallons of gas used
# Write a program that asks the user for the number of miles driven and the 
# gallons of gas used.
# It should calculate the car’s MPG and display the result.
miles_driven = float(input('Enter the number of miles you have driven'))
gallons_of_gas = float(input('Enter the number of gallons of gas used'))
mpg = miles_driven / gallons_of_gas
print("The car's MPG is", mpg)
