year = int(input("Enter a year: "))

if (year % 4 == 0 and year%400 == 0):
    print("yes")
else:
    print("no")
    