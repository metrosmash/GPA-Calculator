from time import sleep
from subprocess import call

call('color 0a', shell=True)

# this is to collect the persons scores and their respective units
print('GPA CALCULATOR ')
print(
    'PLEASE INPUT YOUR SCORES AND THE RESPECTIVE UNIT OF EACH OF YOUR  COURSES  IF YOU HAVE NONE PLEASE INPUT ZERO (0)')
sub1 = int(input("Score-1-"))
sub1ui = int(input("unit-"))
sub2 = int(input("score-2-"))
sub2ui = int(input("unit-"))
sub3 = int(input("score-3-"))
sub3ui = int(input("unit-"))
sub4 = int(input("score-4-"))
sub4ui = int(input("unit-"))
sub5 = int(input("score-5-"))
sub5ui = int(input("unit-"))
sub6 = int(input("score-6-"))
sub6ui = int(input("unit-"))
sub7 = int(input("score-7-"))
sub7ui = int(input("unit-"))
sub8 = int(input("score-8-"))
sub8ui = int(input("unit-"))
sub9 = int(input("score-9-"))
sub9ui = int(input("unit-"))
sub10 = int(input("score-10-"))
sub10ui = int(input("unit-"))
sub11 = int(input("score-11-"))
sub11ui = int(input("unit-"))

# The Errors that occur if the value inputted are zero must be overridden so this piece of code will do the work
try:
    print(" zero's missed")
except:
    print("zero's missed")
finally:
    print("zero's missed")

# just for effects
print("loading .....")
sleep(5)
print("loaded ")
sleep(0.5)

# the (A,b,c,d,e,f) and their values (5,4,3,2,1,0)
A = 5
B = 4
C = 3
D = 2
E = 1
F = 0


# the function for converting the scores into degrees(a,b,c,d,e) and their corresponding values (5,4,3,2,1,0)
def gpa(num):
    if num >= 70:
        num = A
        return A


    elif num >= 60 and num <= 69:
        num = B
        return B


    elif num >= 50 and num <= 59:
        num = C
        return C


    elif num >= 40 and num <= 49:
        num = D
        return D


    elif num >= 0 and num <= 39:
        num = F
        return F


    else:
        print(".......")


# the calculation of the product of the unit against the score of the person
sub1u = gpa(sub1) * sub1ui
sub2u = gpa(sub2) * sub2ui
sub3u = gpa(sub3) * sub3ui
sub4u = gpa(sub4) * sub4ui
sub5u = gpa(sub5) * sub5ui
sub6u = gpa(sub6) * sub6ui
sub7u = gpa(sub7) * sub7ui
sub8u = gpa(sub8) * sub8ui
sub9u = gpa(sub9) * sub9ui
sub10u = gpa(sub10) * sub10ui
sub11u = gpa(sub11) * sub11ui

# now to calculate the gpa of this person
Esum = sub1u + sub2u + sub3u + sub4u + sub5u + sub6u + sub7u + sub8u + sub9u + sub10u + sub11u
Esumu = sub1ui + sub2ui + sub3ui + sub4ui + sub5ui + sub6ui + sub7ui + sub8ui + sub9ui + sub10ui + sub11ui
GPA = float(Esum / Esumu)
if GPA >= 4.5:
    print(str(GPA) + "- First class")
elif GPA <= 4.49 and GPA >= 3.5:
    print(str(GPA) + "- Second class upper ")
elif GPA <= 3.49 and GPA >= 2.4:
    print(str(GPA) + "- Second class lower  ")
elif GPA <= 2.39 and GPA >= 1.50:
    print(str(GPA) + "- Third class")
elif GPA <= 0.5 and GPA >= 1.49:
    print(str(GPA) + "- Probation")
else:
    print(",..,..,.,")
print(" Thanks for using this open source script feel free to modify \n all credits to 'Metro'")
print("press  any key to continue ......")
# TO KEEP THE TERMINAL OPEN SO THE PRESON CAN CHECK THROUGH
input()
