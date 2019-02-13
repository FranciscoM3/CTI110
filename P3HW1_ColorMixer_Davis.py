
# CTI-110 
# P3HW1 - Color Mixer 
# Francisco Davis 
# 12FEB2019
#
# Input two primary colors
# Convert "if-elif-else" Compound Boolean expression \
# using logical operators to determine primary color mixes
# Print color mixes
# Print "else" statement as an error of mis-inputted primary colors.



color1 = input('Enter the first color (red, blue, yellow): ')

color2 = input('Enter the second color (red, blue, yellow): ')



if color1 == 'red' and color2 == 'blue' or \
   color1 == 'blue' and color2 == 'red':
    print (color1 + ' mixes with ' + color2 + ' to make the color purple!')
    
elif color1 == 'red' and color2 == 'yellow' or \
     color1 == 'yellow' and color2 == 'red':
    print (color1 + ' mixes with ' + color2 + ' to make the color orange!')
    
elif color1 == 'blue' and color2 == 'yellow' or \
     color1 == 'yellow' and color2 == 'blue':
    print (color1 + ' mixes with ' + color2 + ' to make the color green!')

else:
    print('One or both primary colors, "' + color1 + '/' + color2 + \
          '", are not recognized.')
