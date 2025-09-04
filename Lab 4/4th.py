my_list=[10,20,30,40,20,50,10]
freq={}
for item in my_list:
    freq[item]=freq.get(item,0)+1
print(freq)