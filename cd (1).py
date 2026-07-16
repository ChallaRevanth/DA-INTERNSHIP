#write a python program to display only odd digits in a given number 1234
number = 1234
for digit in str(number):
    if int(digit) % 2 != 0:
        print(digit,end='')
