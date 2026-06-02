import array as arr

a = arr.array('i', [1,2,3])
for i in range(0, 3):
    print(a[i])

a = arr.array('d', [1,2,3])
for i in range(0, 3):
    print(a[i])

a.insert(0,100)
print(a)
a.append(32232424)
print(a)