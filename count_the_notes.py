a = int(input("amount to withdraw?"))
notes100 = a//100
notes50 = ((a%100)//50)
notes10 = (((a%100)%50)//10)
print(notes100, notes50, notes10)
remaining_amount = (((a%100)%50)%10)
print(remaining_amount)