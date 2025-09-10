#Write a Python program to find the product of the units digits in the numbers of a given list.
#Input: [12, 23] Output:6

numbers=[12,23]
product=1
for n in numbers:
    last_digit=n%10   
    product=product*last_digit   
print(product)
