#user input (first number, second number, operators)

#History Display

history = []


while True:
    try:
        first_num = float(input("Enter your first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        second_num = float(input("Enter your second number: "))


        if operator == "+":
           result = first_num + second_num
        elif operator == "-":
            result = first_num - second_num
        elif operator == "*":
            result= first_num * second_num
        elif operator == "/":
            result = first_num / second_num

        else:
            print("Error, Invalid operator")

    except ValueError:
        print("Please enter valid number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    #history append
    calculation = f"{first_num} {operator} {second_num} = {result}"
    print(f"Answer :{result}")

    history.append(calculation)

    restart= input("Do you want to calculate again? (yes/no)").lower()
    if restart == "no":
        break
