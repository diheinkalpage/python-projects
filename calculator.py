def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def div(a, b):
    return a/b
def mult(a, b):
    return a*b

print("Enter a choice, use the corresponding number to pick. 1 = addition. 2 = subtraction. 3 = division. 4 = multiplictaion.")
numchoice = int(input("Pick here:    "))
num1 = float(input("Enter a number: ")) 
num2 = float(input("Enter a another number: ")) 

if numchoice == 1:
    print(add(num1, num2))

elif numchoice == 2:
    print(sub(num1, num2))

elif numchoice == 3:
    print(div(num1, num2))

elif numchoice == 4:
    print(mult(num1, num2))

else:
    print("Invalid choice.")

