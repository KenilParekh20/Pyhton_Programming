import csv
with open("F:\SEMESTER\python\data-1.csv",'r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)