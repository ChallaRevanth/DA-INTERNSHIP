#write a python program to display product of even numbers in a given number 32456
number = 32456
product = 1
while number!=0:
    digit = number % 10
    if digit % 2 == 0:
        product *= digit
    number //= 10
print("Product of even digits:", product)