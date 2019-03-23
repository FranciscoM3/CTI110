# Develop a program that accumulates a collected bug total
# 18Mar2019
# CTI-110 P4T2 - Bug Collector
# Francisco Davis
#



total= 0
# Using a for loop ask for bugs collected in 5 days
for d in range(5):
    print('Enter bugs collected today')
    bugs= int(input())
    total+= bugs

# Display accumulated total
print('In 5 days you collected', total, 'bugs.')

