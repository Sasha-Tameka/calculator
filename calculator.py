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

    #Ask user if they want to see history
    show_history = input("Show calculation history? yes/no: ")
    if show_history.lower() == "yes":
        print(f"\n History Calculation: ")
        for i, cal in enumerate(history,1):
             print(f"{i}. {cal}")

    #Ask user if they want to remove history
    remove_history = input("Would you like to remove history? (all/specific/no):")

    if remove_history.lower()== "specific":
        if len(history)== 0:
            print("No history to remove")




    restart= input("Do you want to calculate again? (yes/no)").lower()
    if restart == "no":
        break
