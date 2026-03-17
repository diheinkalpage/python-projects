rows=int(input("Enter the number of rows to make a floyd triangle:  "))
x = 1
for i in range(rows):
    for j in range(i + 1):
        print(x,end=" ")
        x+=1
    print()
