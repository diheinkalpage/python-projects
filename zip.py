name=['Nico', 'Lachlan', 'Colin', 'Ethan']
roll=[3,8,1,9]
mapped=zip(name, roll)
print(mapped)
mapped1=zip(name, roll[::-1])
print(list(mapped))
print(list(mapped1))