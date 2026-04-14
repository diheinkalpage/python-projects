try:
    num1,num2=eval("Enter 2 numbes seperated by a comma:  ")
    ans = num1 + num2
    print(ans)
except SyntaxError:
    print("Numbers must be seperated by a comma")