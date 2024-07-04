
list1 = [("WorkOut", True), ("Drink Water", False)]

check = ""
while check != "exit":
    print("Press 1 if you want to enter the Task")
    print("Press 2 if you want to update the task")
    print("Press 3 if you want to update the status")
    print("Press 4 if you want to delete the task")
    print("Press 5 if you want to display the list")
    print("Press 6 if you want to exit")

    valid_input = False
    while not valid_input:
        try:
            a = int(input("Enter a number: "))
            valid_input = True
        except ValueError:
            print("Invalid Input. Please enter a valid integer.")

    if a == 1:
        task = input("Enter The task: ")
        status_input = input("Write True if the work is complete and False if not: ")
        status = status_input == "true"
        list1.append((task, status))  # Add task to list1

    elif a==2:
        task = input("Enter The task Name you want to update: ")
        status_input = bool(("Write True if the work is complete and False if not: "))
        try:
            index = list1.index((task, True))
        except ValueError:
            try:
                index = list1.index((task, False))
            except ValueError:
                print("Task not found.")
            continue
        x,y=list1[index]
        str=input("Update the Task Name: ")
        list1[index] = (str,y)

    elif a==3:
        task = input("Enter The task Name whose status you want to update: ")
        status_input = bool(("Write True if the work is complete and False if not: "))
        try:
            index = list1.index((task, True))
        except ValueError:
            try:
                index = list1.index((task, False))
            except ValueError:
                print("Task not found.")
            continue
        x,y=list1[index]
        if y is True:
            list1[index] = (x,False)
        else:
            list1[index] = (x,True)

    elif a==4:
        task = input("Enter The task Name you want to update: ")
        status_input = bool(("Write True if the work is complete and False if not: "))
        index = list1.index((task, True))
        list1.pop(index)


    elif a == 5:
        if not list1:
            print("The list is empty.")
        else:
            print("The list you have".center(40,'-'))
            i = 1
            for task, status in list1:
                print(f"{task} and {status}")
                i += 1

    elif a == 6:
        check = "exit"
        print("Exiting the program.")

    else:
        print("Invalid input. Please enter a number between 1 and 6.")

print("Program ended.")

print(list1)