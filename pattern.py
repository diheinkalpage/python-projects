rows=int(input("Enter the number of rows to make a right angle triangle:  "))
for i in range(rows):
    for j in range(i + 1):
        print("☆",end=" ")
    print()