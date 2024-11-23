from time import sleep
from subprocess import call

call('color 0a', shell=True)
'''This Variant of the gpa calculator asks the user for the number of subjects taken then 
collects the score and units then it calculates the gpa and presents it to the user.
# this is to collect the persons scores and their respective units '''
print('GPA CALCULATOR ')
print(
    'PLEASE INPUT YOUR SCORES AND THE RESPECTIVE UNIT OF EACH OF YOUR  COURSES  IF YOU HAVE NONE PLEASE INPUT ZERO (0)')

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


# Function to categorize the gpa (first class to second class)
def gpa_stats(GPA):
    if GPA >= 4.5:
        print(str(GPA) + "- First class")
    elif 4.49 >= GPA >= 3.5:
        print(str(GPA) + "- Second class upper ")
    elif 3.49 >= GPA >= 2.4:
        print(str(GPA) + "- Second class lower  ")
    elif 2.39 >= GPA >= 1.50:
        print(str(GPA) + "- Third class")
    elif 0.5 >= GPA >= 1.49:
        print(str(GPA) + "- Probation")
    else:
        print(",..,..,.,")


subjectLimit = int(input('How many subjects did you register? '))
numberLimit = 0
totalSubUnit = 0
totalSubProduct = 0
while numberLimit != subjectLimit:
    numberLimit += 1
    subject = int(input("Score on Subject> "))
    subjectUnit = int(input("Subject Unit>  "))
    totalSubUnit += subjectUnit
    subjectData = gpa(subject) * subjectUnit
    totalSubProduct += subjectData

gpa = float(totalSubProduct / totalSubUnit)
gpa_stats(gpa)

print(" Thanks for using this open source script feel free to modify \n all credits to 'Metro'")
print("press  any key to continue ......")
# TO KEEP THE TERMINAL OPEN SO THE PRESON CAN CHECK THROUGH
input()
