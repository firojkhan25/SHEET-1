a = int(input("enter the first angle\n:"))
b = int(input("enter the second angle\n:"))
c = int(input("enter the third angle\n:"))
if a+b+c == 180:
    if a == 90 or b == 90 or c== 90:
        print("right angle")
    elif a > 90 or b > 90 or c > 90:
         print("obtuse angle")
    else :
        print("acute angle")
else:
    print("invalid angle") 

