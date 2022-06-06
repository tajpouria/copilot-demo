# read a number from user
# read an operator from user
# calculate the result
# print the result
while True:
    a = int(input("Enter a number: "))
    operator = input("Enter an operator: ")
    b = int(input("Enter a number: "))
    # throw an error if the user enters a non-number
    if type(a) != int or type(b) != int:
        raise ValueError("You must enter a number")

    if operator == "+":
        print(a + b)
    elif operator == "-":
        print(a - b)
    elif operator == "*":
        print(a * b)
    elif operator == "/":
        print(a / b)
    elif operator == "%":
        print(a % b)
    elif operator == "**":
        print(a**b)
    else:
        print("Invalid operator")

    # ask the user if they want to continue
    continue_ = input("Continue? (y/n): ")
    if continue_ == "n":
        break
    elif continue_ == "y":
        continue
