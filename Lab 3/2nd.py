string=input("Enter the string:")
print(string)
reversed=string[::-1]
print("Original string ",string)
print("Reversed string ",reversed)
if string==reversed:
    print("String is palindrome")
else:
    print("String is not palindrome")