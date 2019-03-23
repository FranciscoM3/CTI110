# Generate the sum of all positive numbers
# 19MAR2019
# CTI-110 P4HW3 - Sum of Numbers
# Francisco Davis
#
# Ask the user to input the first nuimber.
# Use a acumulator variable set at 0.
# Using the while loop for as long as a positive number is
# entered it will acumulate.
# Display results


PosNum= float(input('Enter the first positive number: '))
total= 0

while PosNum >= 0:
    total= total + PosNum
    PosNum= float(input('Enter the next positive number, or enter a negative'
    '\nnumber to exit program: '))

print('\nThe sum of all positive numbers is:', total)
