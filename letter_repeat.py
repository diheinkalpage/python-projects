word = input("Enter a word:  ")
letter = input("Enter a letter that is in the word")
count = 0

for i in word:
    if i == letter:
        count=count+1
    

print("Number of times",letter,"is present in",word,"=",count)