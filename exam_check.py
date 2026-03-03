medicalcause = input("Do you have a medical cause? Y for yes and N for no:  ")
if medicalcause == "Y" or medicalcause == 'y':
    print("You are allowed to take the exam")

elif medicalcause == "N" or medicalcause == 'n':
    attendancepercentage = int(input("What is your attendance percentage?:  "))
    if attendancepercentage > 75 :
        print("You are allowed to take the exam")
    elif  attendancepercentage <= 75 :
        print("You are not allowed to take the exam")
    else:
         print("Invalid")
else:
         print("Invalid")
