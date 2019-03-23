# Develop a program that converts 100 to 300 pounds in to kilograms
# by increments of 10.
# 18Mar2019
# CTI-110 P4HW2 - Pounds to Kilos Table
# Francisco Davis
#
# Display a heading of the units being used
# Use a for loop to create a range of 100-300 pounds by increments of 10
# Create the conversion that will be used for pounds to kilos
# Display results 





print('Pounds\tKilograms')
print('_________________')


for lbs in range(100,301,10):
    kg= lbs/2.2046
    print(lbs, '\t', format(kg, '.4f'))
