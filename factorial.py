def factor(x):
    if x==1 or x == 0:
        return 1
    else:
        return x*factor(x-1)
n = int(input("Enter a number to find the factorial:  "))
print(factor(n))