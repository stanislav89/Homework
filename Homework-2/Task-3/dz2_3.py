fizz = int(input("Enter first number: "))
buzz = int(input("Enter second number: "))
third_ = int(input("Enter third number: "))

schet = 0
while schet < third_:
    schet += 1
    if schet % fizz == 0 and schet % buzz == 0:
        print('FB')
    elif schet % fizz == 0:
        print('F')
    elif schet % buzz == 0:
        print('B')
    else:
        print(schet)
