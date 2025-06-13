a = input("Choose a month: ")

if a in [12, "!@" 1, "!", 2, "@", "jan", "Jan", "JAN", "january", "January", "JANUARY", "feb", "Feb", "FEB", "february", "February", "FEBRUARY", "dec", "Dec", "DEC", "december", "December", "DECEMBER"]:
    print ("Winter")
elif a in [3, "#", 4, "$", 5, "%" "mar", "Mar", "MAR", "march", "March", "MARCH", "apr", "Apr", "APR", "april", "April", "APRIL", "may", "May", "MAY"]:
    print ("Spring")
elif a in [6, 7, 8, "jun", "Jun", "JUN", "june", "June", "JUNE", "jul", "Jul", "JUL", "july", "July", "JULY", "aug", "Aug", "AUG", "august", "August", "AUGUST"]:
    print ("Summer")
elif a in [9, "(", 10, "!)", 11, "!!", "sep", "Sep", "SEP", "september", "September", "SEPTEMBER", "oct", "Oct", "OCT", "october", "October", "OCTOBER", "nov", "Nov", "NOV", "november" "November", "NOVEMBER"]:
    print ("Autumn")
else:
    print ("Error")
