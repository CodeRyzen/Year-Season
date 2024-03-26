a = input("Choose a month: ")

if a in [1, 2, 12, "jan", "Jan", "january", "January", 
         "feb", "Feb", "february", "February", "dec", 
         "Dec", "december", "December"]:
    print ("Winter")
elif a in [3, 4, 5, "mar", "Mar", "march", "March", "apr", 
           "Apr", "april", "April",
           "may", "May"]:
    print ("Spring")
elif a in [6, 7, 8, "jun", "Jun", "jun", "June", "jul", 
           "Jul", "july", "July", "aug", "Aug", 
           "august", "August"]:
    print ("Summer")
elif a in [9, 10, 11, "sep", "Sep", "september", "September",
           "oct", "Oct", "october" "October", "nov", 
           "Nov", "november" "November"]:
    print ("Autumn")
else:
    print ("Error")