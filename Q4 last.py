num = int(input("enter a number\n:"))
ld = num % 10
if ld == 5 and num % 7 == 0:
    print("yes")
else:
    print("no")