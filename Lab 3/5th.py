sentence=input("Enter a sentence:")
words=sentence.strip().split()
longest_word=max(words,key=len)
if words:
    print("Length of last word ",len(words[-1]))
else:
    print("Length ",len(longest_word))
    