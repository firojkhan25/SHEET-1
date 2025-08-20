D = int(input("Enter a number (1-7): "))

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if 1 <=  D <= 7:
    print("Day = :", days[D - 1])
else:
    print("Invalid number!")
