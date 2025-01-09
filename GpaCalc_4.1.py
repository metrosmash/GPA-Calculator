import pandas as pd
import numpy as np

'''This Variant of the gpa calculator uses a list to calculate the gpa (to excel document ).
# this is to collect the persons scores and their respective units '''
print('GPA CALCULATOR ')
print(
    'PLEASE INPUT YOUR SCORES AND THE RESPECTIVE UNIT OF EACH OF YOUR  COURSES  IF YOU HAVE NONE PLEASE INPUT ZERO (0)')

# what pandas is suposed to do is to load the data down from the .csv file and then read the data, calculate the GPA then
# return the CGPA to the csv file and then do this for each line in the csv file
# The extracting part one will extract this details from the excel 
subject = [98, 76, 74, 98, 80, 86, 88, 74, 76, 98, 74]
subjectUnit = [3, 2, 1, 3, 2, 1, 3, 2, 2, 2, 1]
# PART ONE
filepath = 'data\StudentScore.csv'
csvFile = pd.read_csv(filepath)
# PART TWO
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
    elif 60 <= num <= 69:
        num = B
        return B
    elif 50 <= num <= 59:
        num = C
        return C
    elif 40 <= num <= 49:
        num = D
        return D
    elif 0 <= num <= 39:
        num = F
        return F
    else:
        print(".......")


# Function to categorize the gpa (first class to second class)
def gpa_stats(var):
    if var >= 4.5:
        print(f'{var} - First Class ')
    elif 3.5 <= var <= 4.49:
        print(f'{var} - Second Class Upper')
    elif 2.5 <= var <= 3.49:
        print(f'{var} - Second Class Lower')
    elif 1.50 <= var <= 2.49:
        print(f'{var} - Third Class ')
    elif 0.5 <= var <= 1.49:
        print(f'{var} - Probation ')
    elif 0.0 <= var <= 0.49:
        print(f'{var} - Probation 2')
    else:
        print(f'{var} - error here')


subject_limit = len(subject)
number_limit = 0
totalSubUnit = 0
totalSubProduct = 0
try:
    while number_limit != subject_limit:
        number_limit += 1
        subject1 = subject[number_limit]
        subject_unit1 = subjectUnit[number_limit]
        totalSubUnit += subject_unit1
        subjectData = gpa(subject1) * subject_unit1
        totalSubProduct += subjectData
        gpa = float(totalSubProduct / totalSubUnit)
        gpa_stats(gpa)
except TypeError:
    pass

# The next part is to read an excel document and then use pandas to take in the details and then work on it and produce the answer
