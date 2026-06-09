def square(n):
    return n*n


numbers=(4,8,2,6,9)
result = map(square, numbers)
print(result)
print(list(result))