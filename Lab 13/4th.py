with open("F:/SEMESTER/python/file1.txt","r") as file1:
    data1=file1.read()
with open("F:/SEMESTER/python/file2.txt","r") as file2:
    data2=file2.read()
    
with open("merged.txt","w") as merged:
    merged.write(data1) 
    merged.write(data2) 