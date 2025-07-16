#user input (first number, second number, operators)


while True:
    try:
        first_num = float(input("Enter your first number: "))
        second_num = float(input("Enter your second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator == "+":
            print(f"Answer: {first_num + second_num}")
        elif operator == "-":
            print(f"Answer:  {first_num - second_num}")
        elif operator == "*":
            print(f"Answer: {first_num * second_num}")
        elif operator == "/":
            print(f"Answer: {first_num / second_num}")

        else:
            print("Error, Invalid operator")

    except ValueError:
        print("Please enter valid number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    restart= input("Do you want to calculate again? (yes/no)").lower()
    if restart == "no":
        break
