def month():
    n = int(input("Enter month number: "))
    month_name = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    return month_name[n-1]

print(month())