def cube(number):
    return number*number*number
def three(number):
    if number %3 == 0:
        return cube(number)
    else:
        return False
n = int(input("Enter a number to cube:  "))
print(three(n))