try:
    age = int(input("Enter your age:  "))
    if (age>18):
        print("Your age is valid.")
    else:
        raise ValueError
except ValueError:
    print("Your age is invalid.")
finally:
    print("Thank you")
