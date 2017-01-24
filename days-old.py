"""Lenghty but robust code for finding how old you are in days, simple exercise in loops
All the commented out code is just random things i use to test on the fly. Sorry it's messy but i keep it there for when i make changes """


def lenmonth(month, year):
    thirtyone = [1,3,5,7,8,10,12]
    thirty = [4,6,9,11]
    
    if month == 2: 
        if year%4 != 0:
            return 28
        elif (year%100 != 0):
            return 29
        elif year%400 != 0:
            return 28
        else:
            return 29
            
    if month in thirty:
        return 30
    elif month in thirtyone:
        return 31
        
def lenyear(year):
    if year%4 == 0 or (year%100 == 0 and year%400 == 0):
        return 366
    else:
        return 365
    
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    days = 0
    cm = 0
    cy = 0
    
    if(year2 == year1):
        if(month2 == month1):
            days = day2 - day1
        
        else:
            days = lenmonth(month1,year1) - day1
            cm = month1+1
            cy = year1
            while(cm < month2):
                days = days + lenmonth(cm, cy)
                cm = cm+1
            days = days + day2
            
    else:
        days = lenmonth(month1,year1) - day1
        cm = month1+1
        cy = year1 +1
        while(cm <= 12):
            days = days + lenmonth(cm, year1)
            cm = cm+1
        
        while(cy < year2):
            days = days + lenyear(cy)
            cy = cy+1
        cm = 1
        while(cm < month2):
            days = days + lenmonth(cm, year2)
            cm = cm+1
        days = days + day2
    #    if year2-year1 > 1:
    #        days = days+1
    
    return days
        
    
    
    if month1 == 12:
        cm = 1
        cy = year1+1
    else:
        cm = month1+1
        cy = year1
        
#    print cy,cm
 #   print year2, month2
    enter = False
    
   # print days
    
    while cy <= year2:
        if cm == month2 and cy == year2:
            break
        enter = True
        days = days + lenmonth(cm,cy)
        #print lenmonth(cm,cy)
        #print days
        cm = cm+1
        if cm == 13:
            cm = 1
            cy = cy+1
        
    
    days = days + day2
    #if enter:
       # days = days +1
    
    return days
            
            
        
    
   
        
# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585),
                  ((1900,1,1,1999,12,31), 36523)]
    #test_cases = [((2011,6,30,2012,6,30), 366)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
    #    if result != answer:
     #       print "Test with data:", args, "failed"
      #  else:
       #     print "Test case passed!"
        print result


test()
