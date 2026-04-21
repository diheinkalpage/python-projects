import random
print("Hi There! Welcome to the most jaw-dropping, heart-stopping, mind-bending number guessing game there is to offer! My name is Computor, and i'm your host, ready to show you how this game works")
print("\nIt's very simple, just guess a number from 1 to 100 and see how your luck prevails. By clicking that run button, you have agrred to the terms and conditions listed below","\nhwdglGASHCLHASHCLIhduiahlicsc;UJAO;UCHA;ouduoyui;HEUIFHuofhUHFI;UehfUHFI;UhfuiSHFU;UEU;JFHUIEwfjkehfuo;eNEFKJEUFJEJFO;IEWJFAJFUOEJFLKAEFOIWIF;OIAWEJF'IEAIDWJF;OIWJFOIEUFJIEwjfo;ewjfoejfoi;ewjflkefjkefhuiehfiueHFJKhduiejwfjejjfejefeFEFE")
cg = random.randint(1,100)
ug = int(input("Alright let us start! Enter your guess:  "))
if ug==cg:
    print("CONGRATULATIONS! YOU GUESSED CORRECT. Now for your GRAND PRIZE! YOU WON...")
    sd = input("Do you want to know? y for yes and n for no. Make sure that they are lower case if you want your GRAND PRIZE")
    if sd == "y" or sd == "n":
        print("YOUR GRAND PRIZE IS...","\nZERO DOLLARS. if you typed n too bad.")
else:
    print("OH NO, you guessed wrong. try again")
    
