English = int(input("enter the  eng marks\n:"))
Hindhi = int(input("enter the  hin marks\n"))
Math = int(input("enter the math marks\n"))
marks = English+Hindhi+Math
per=marks*100/300
print("the percentage is ",per)
if per < 25:
    print("Grade: D")
elif per <= 45:
    print("Grade: C")
elif per <= 65:
    print("Grade: B")
elif per <= 85:
    print("Grade: A")
else:
    print("Grade: A+")
