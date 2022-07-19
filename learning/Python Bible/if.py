num1 = 100
num2 = 100

if num1 > num2:
    print("num1 is bigger than num2")
elif num2 > num1:
    print("num2 is bigger than num1")
else:
    print("Both numbers are equal")



C = 6
D = 2
if (C > 5 and D > 5) or (C > 1 and D > 1):
    print("It worked")

if not ((C > 5 and D > 5) or (C > 1 and D > 1)):
    print("It won't work")