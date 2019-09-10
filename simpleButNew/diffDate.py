from datetime import date
print("Enter the dates in the form of (YYYY,MM,DD)")
date1 = str(input("Enter date 1:"))
date2 = str(input("Enter date 2:"))
#diff = date2-date1
diff = (date(date2)) - (date(date1))
print(diff.days)


