# Determine greater or equal areas of two rectangles.
# 12FEB2019
# CTI-110 P3T1 - Areas of Rectangles
# Francisco Davis
#
# Input the length and width for rectangle 1
# Input the length and width for rectangle 2
# Calculate the area for both rectangles
# Use the "if/else" functions to print greater than or \
# equal to areas of both rectangles
#


length1 = float(input('Enter length of rectangle 1: '))

width1 = float(input('Enter width of rectangle 1: '))


length2 = float(input('Enter length of rectangle 2: '))

width2 = float(input('Enter width of rectangle 2: '))


area1 = length1 * width1

area2 = length2 * width2


if area1 > area2:
    print('Rectangle 1 has the greater area.')
else:
    if area2 > area1:
        print ('Rectangle 2 has the greater area.')
    else:
        print ('Both rectangles have the same area.')



# Also can be shown as:
# "if area1 > area2:
#    print('Rectangle 1 has the greater area.')
# elif area2 > area1:
#    print ('Rectangle 2 has the greater area.')
# else:
#    print ('Both rectangles have the same area.')"
