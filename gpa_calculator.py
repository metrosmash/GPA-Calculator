# GPA CALCULATOR FOR FUOYE

# for color
from subprocess import call

call('color a', shell=True)
#this sets the color to light green
print(" mmGmm ")
print(" mmmPmmm ")
print(" mmmmAmmmm ")
print(" GPA Calculator version 1 \n may 2021 \n By Metro  ")
print(" Please note this gpa calculator is for 100 level students only ")
print( " welcome please enter your details ")



#asking for the scores on the course
chm101 = int(input ('chm 101 ?-'))
mth101 = int(input("mth 101?-"))
mth103 = int(input("mth 103?-"))
chm107 =int(input("chm107?-"))
cpe101 =int(input('cpe101?-'))
gst101 =int(input("gst101?-"))
gst105 =int(input("gst105?-"))
gst103 =int(input("gst103?-"))
phy101 =int(input("phy101?-"))
phy103 =int(input("phy103?-"))
phy107 =int(input("phy107?-"))
# values
A = 5
B = 4
C = 3
D = 2
E = 1
F = 0
# the function for converting the scores into degrees(a,b,c,d,e) and thier coresponding values (5,4,3,2,1,0)
def gpa(num):
    if num >= 70:
        num = A
        return A
        print("A")

    elif num >= 60 and num <= 69:
        num = B
        return B
        print("B")

    elif num >= 50 and num <= 59:
        num = C
        return C
        print("C")

    elif num >= 40 and num <= 49:
        num = D
        return D
        print("D")

    elif num >= 0 and num <= 39:
        num = F
        return F
        print("F")

    else:
        print(".......")



# the calculation of the product of the unit against the score of the person
chm1u = gpa(chm101) *3
mth1u = gpa(mth101) *3
mth3u = gpa(mth103) *3
chm7u = gpa(chm107) *1
cpe1u = gpa(cpe101) *2
gst1u = gpa(gst101) *2
gst5u = gpa(gst105) *1
gst3u = gpa(gst103) *2
phy1u = gpa(phy101) *3
phy3u = gpa(phy103) *2
phy7u = gpa(phy107) *1
#now to calculate the gpa of this person
Esum =chm7u+chm1u+mth3u+mth1u+cpe1u+gst3u+gst5u+gst1u+phy7u+phy3u+phy1u
Esumu = 23
GPA = float(Esum/Esumu)
if GPA >=4.5:
    print(str(GPA) + "- First class")
elif GPA <= 4.49 and GPA >= 3.5 :
    print(str(GPA) + "- Second class upper ")
elif GPA <= 2.5 and GPA >= 3.49 :
    print(str(GPA) + "- Second class lower  ")
elif GPA <=1.5 and GPA >= 2.49:
    print(str(GPA) + "- First class")
elif GPA <= 0.5 and GPA >= 1.49:
    print (str(GPA) + "- Probation")
else:
    print(",..,..,.,")
print (" Thanks for using this open source script feel free to modify \n all credits to 'Metro'")
input()