temp = int(input("Enter a number:  "))
count = 0
while temp > 0:
    digit = temp % 10
    count=count+1
    temp //= 10

print("Number of digits:",count)
