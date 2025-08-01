#user input (first number, second number, operators)

#History Display

history = []


while True:
    try:
        first_num = float(input("Enter your first number: "))
        print("--------------------------")
        operator = input("Enter operator (+, -, *, /): ")
        print("--------------------------")
        second_num = float(input("Enter your second number: "))
        print("--------------------------")



        if operator == "+":
           result = first_num + second_num
        elif operator == "-":
            result = first_num - second_num
        elif operator == "*":
            result= first_num * second_num
        elif operator == "/":
            if second_num == 0:
                print("Error: Cannot divide by zero!")
                continue
            result = first_num / second_num

        else:
            print("Error, Invalid operator, Please use +, -, *, or /")
            continue

     # history append
        calculation = f"{first_num} {operator} {second_num} = {result}"
        print(f"Answer : {result}")
        history.append(calculation)


    except ValueError:
        print("Please enter valid number")
        continue

    #Ask user if they want to see history
    show_history = input("Show calculation history? yes/no: ")
    print("--------------------------")
    if show_history.lower() == "yes":
        if history:
            print(f"\n History Calculation: ")
            for i, cal in enumerate(history,1):
                print(f"{i}. {cal}")
                print("--------------------------")
        else:
            print("No history available")


    #Ask user if they want to remove history
    remove_history = input("Would you like to remove history? (all/specific/no):")

    if remove_history.lower()== "specific":
        if len(history)== 0:
            print("No history to remove")
        else:
            print(f"\n History Calculation: ")
            for i, cal in enumerate(history, 1):
                print(f"{i}. {cal}")

        #get user's choice of which to remove
        try:
            choice = int(input("\nEnter number to remove: "))
            if 1<= choice <= len(history):
                removed = history.pop(choice - 1)
                print(f"✓ Removed: {removed}")
            else:
                print("Invalid number")
        except ValueError:
            print("Please enter a valid number ")








    restart= input("Do you want to calculate again? (yes/no)").lower()
    if restart == "no":
        break
