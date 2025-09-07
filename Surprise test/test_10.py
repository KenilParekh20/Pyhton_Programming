#10. Write a Python program to find missing numbers from a list.
#Input:[1,2,5,10,11,14,17,20]
#Output: [3,4,6,7,8,9,12,13,15,16,18,19]

numbers = [1,2,5,10,11,14,17,20]
missing=[]  
for i in range(1,21):  
    if i not in numbers:  
        missing.append(i) 
print(missing)
