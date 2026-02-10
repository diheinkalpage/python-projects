"""

Raj scored 40, 70, 50 and 60 out of 100 in maths,

science, Hindi and English. Find the percentage he

got?print("Enter Marks Obtained in 4 Subjects: ")"""

maths = int(input("maths:"))
science = int(input("science:"))
hindi = int(input("hindi:"))
english = int(input("english:"))
sum = maths+science+hindi+english
perc = (sum/400)*100
print(perc)
