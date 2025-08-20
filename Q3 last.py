num = int(input("enter a number\n:"))
ld = num % 10
if ld == 4 and num % 3 == 0 :
    print("yes")
else:
    print("no")