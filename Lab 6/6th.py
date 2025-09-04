num=int(input("Enter a no:"))
n=abs(num)
product=1
while n>0:
    digit=n%10
    product*=digit
    n //= 10
print("Product of digits:",product)