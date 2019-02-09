#Calculate the total amount of a meal purchased including tip
#08Feb2019
#CTI-110 P2HW2 - Meal Tip Calulator
#Francisco Davis
#
#Input float variable for meal price
#Calculate percentage of tip for 15%, 18%, and 20%
#Display the formatted total price of meal with tip

print (' ')

meal_price = float (input ('Enter the price of the meal: $'))

tip1 = meal_price * 0.15

tip2 = meal_price * 0.18

tip3 = meal_price * 0.2

print (' ')

print ("""  The total price of the meal for the following tips
  are as followed:""")

print (' ')

print (' For 15% it is $', format (tip1 + meal_price, ',.2f'), sep='')
print (' For 18% it is $', format (tip2 + meal_price, ',.2f'), sep='')
print (' For 20% it is $', format (tip3 + meal_price, ',.2f'), sep='')
