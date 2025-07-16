#user input (first number, second number, operators)
try:
    first_num = float(input("Enter your first number: "))
    second_num = float(input("Enter your second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        print(first_num + second_num)
    elif operator == "-":
        print(first_num - second_num)
    elif operator == "*":
        print(first_num * second_num)
    elif operator == "/":
        print(first_num / second_num)
    else:
        print("Error, Invalid operator")

except ValueError:
    print("Please enter valid number")
