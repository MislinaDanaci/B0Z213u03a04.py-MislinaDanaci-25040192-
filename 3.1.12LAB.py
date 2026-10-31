year = int (input("enter a year:"))

if year < 1582 :
    print("not within the Gregorian calender period")
else:
    if year % 4 !=0:
        print("common year")
    elif year % 100 !=0:
        print ("leap year")
    elif year % 100 != 0:
        print ("common year")
    else:
        print("leap year")
            
