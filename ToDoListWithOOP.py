class Item:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def display_items(self):
        if self.status==True:
            symbol = "\u2714"

        else:
            symbol = "\u274C"
        print(f"{self.id} {self.name} {symbol} ")



class ToDoList:
    def __init__(self):
        self.items = {}

    def add_item(self, id, item):
        if id not in self.items:
            self.items[id] = item
        else:
            print(f"Item with id {id} is already listed.")

    def display_list(self):
        for item in self.items.values():
            item.display_items()
        print("-" * 40)

    def remeove_item(self, id):
        if id in self.items:
            self.items.pop(id)
        else:
            print(f"Item with id {id} not found.")

    def update_item(self, id, **kwargs):
        if id in self.items:
            if 'name' in kwargs:
                self.items[id].name = kwargs['name']
            if 'status' in kwargs:
                self.items[id].status = kwargs['status']
        else:
            print(f"Item with id {id} not found.")


def check_user_input():

    check_user_input = False
    while not check_user_input:
        try:
            a = int(input("Enter a number between 1 to 6: "))
            check_user_input = True
        except ValueError:
            print("Invalid Input. ")
    return a

def check_id(str):
    check_user_input = False
    while not check_user_input:
        try:
            a = int(input(str))
            check_user_input = True
        except ValueError:
            print("Invalid Input.")
    return a

def check_status():
    while True:
        try:
            status = int(input("Press 1 if the task is completed, press 2 if not completed: "))
            if status == 1:
                return True
            elif status == 2:
                return False
            else:
                print("Invalid input. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input.")

if __name__ == '__main__':

    task1 = Item(1, "Task-1", True)
    task2 = Item(2, "Task 2", False)

    todo_list = ToDoList()

    todo_list.add_item(1,task1)
    todo_list.add_item(2,task2)

    print("Welcome to My ToDOList App".center(80,"-"))

    execute=0
while execute!=6:
    print("Press 1 If you want to enter the task")
    print("Press 2 If you want to display the task")
    print("Press 3 If you want to remove the task")
    print("Press 4 If you want to update the task name")
    print("Press 5 If you want to update the task status")
    print("Press 6 If you want to exit")
    print("-" * 40)

    selected_input=check_user_input()
    print("-" * 40)

    if selected_input==1:
        a=0
        while(a!=-1):

            id=check_id("Enter the id: ")
            print("Enter the task name: ",end="")
            task = input()
            # print("Enter the Status: ")
            status=check_status()
            item=Item(id,task,status)
            todo_list.add_item(id,item)
            print("Do you want to add more items y/n: ")
            check=input()
            a = 0 if check == "y" else -1
        print("Tasks in ToDoList")
        todo_list.display_list()



    if selected_input==2:
        print("Tasks in ToDoList")
        todo_list.display_list()

    if selected_input==3:
        id=check_id("Enter the id of the task you want to remove: ")
        todo_list.remeove_item(id)
        print("Tasks in ToDoList")
        todo_list.display_list()

    if selected_input==4:
        id=check_id("Enter the id of the task you want to update the name: ")
        print("Enter the Name you have to update: ", end="")
        name=input()
        todo_list.update_item(id,name=name)
        print("Tasks in ToDoList")
        todo_list.display_list()

    if selected_input==5:
        id=check_id("Enter the id of the task you want to update the status: ")
        print("Enter the status you have to update: ", end="")
        status=check_status()
        todo_list.update_item(id,status=status)
        print("Tasks in ToDoList")
        todo_list.display_list()

    if selected_input==6:
        execute=6
