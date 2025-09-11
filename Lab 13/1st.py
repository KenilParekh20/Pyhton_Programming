filename="example.txt"
with open("F:\SEMESTER\python\example.txt","r") as file:
    text=file.read()

lines=text.splitlines()
words=text.split()
characters=list(text)

print("Lines:",len(lines))
print("Words:",len(words))
print("Characters:",len(characters))