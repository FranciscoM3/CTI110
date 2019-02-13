# CTI-110
# P3HW2 - MealTipTax
# Francisco Davis
# 13Feb2019
#
# Input float variable for meal price.
# Calculate tax on meal.
# Calculate percentage of tip for 15%, 18%, and 20% on meal.
# Convert "if-elif-else" Compound Boolean expression \
# using logical operators to determine tip factors.
# Display the formatted total price of meal with tip and tax.
# Display "else" statement as an error of an invalid response.

print (' ')
meal_price = float (input ('Enter the price of the meal: $'))

tip = int (input ('Enter the tip percentage you would like to consider: '))


tip1 = meal_price * 0.15

tip2 = meal_price * 0.18

tip3 = meal_price * 0.2

tax = meal_price * 0.07


if tip == 15:
    print ('At 15% the tip is $', format (tip1, ',.2f'), ' and the tax is $', \
           format (tax, ',.2f'), ', bringing your total to $', \
           format (tip1 + tax + meal_price, ',.2f'), sep='')
elif tip == 18:
    print ('At 18% the tip is $', format (tip2, ',.2f'), ' and the tax is $', \
           format (tax, ',.2f'), ', bringing your total to $', \
           format (tip2 + tax + meal_price, ',.2f'), sep='')
elif tip == 20:
    print ('At 20% the tip is $', format (tip3, ',.2f'), ' and the tax is $', \
           format (tax, ',.2f'), ', bringing your total to $', \
           format (tip3 + tax + meal_price, ',.2f'), sep='')
else:
    print('Tip percentage "' + str(tip) + '%" is not valid.')
    
    
