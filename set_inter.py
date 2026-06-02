dan={"Blue", "Black", "Red", "Green", "Teal"}
teacher={"White", "Black", "Red", "Pink"}
print(dan)
print(teacher)
print("Common colors: ", dan.intersection(teacher))
print("All colors: ", dan.union(teacher))
print("Difference 1: ", dan.difference(teacher))
print("Difference 2: ", teacher.difference(dan))
print("Symmetric difference: ", dan.symmetric_difference(teacher))