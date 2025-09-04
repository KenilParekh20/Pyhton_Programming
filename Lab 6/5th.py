num=input("Enter a no:")
if len(num)==1:
    print("Swapped no:",num)
else:
    swapped=num[-1]+num[1:-1]+num[0]
    print("Swapped no:",swapped)