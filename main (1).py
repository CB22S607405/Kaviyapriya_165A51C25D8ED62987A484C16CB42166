#1.2W rite a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements.

year=int(input("Input the Year: "))    
if(year%4==0):                       
    if(year%400==0):                   
        print("Entered Year is a Leap Year.")     
    elif(year%100==0 and year%400!=0):
        print("It is not a Leap Year.")
    else:
        print("Entered Year is a Leap Year.")
else:
    print("Entered Year is not a Leap Year.")