ages=(34,56,34,7,78,35)
for ages in ages:
    if ages<18:
        print(ages, 'Not Allowed')
        exit()
    else:
        print(ages, 'Allowed')