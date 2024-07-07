class Item:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    def display_items(self):
        if self.status==True:
            symbol1="\u2714"
        else:
            symbol1="\u0020"
        print(f"{self.id} {self.name} {symbol1} ")



class ToDoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_list(self):
        for item in self.items:
            item.display_items()
        print("-"*40)
    def remeove_item(self,id):
        for item in self.items:
            if item.id==id:
                self.items.remove(item)
                break

    def update_item_taskName(self,id,name):
        for item in self.items:
            if item.id==id:
                item.name=name
                break

    def update_item_taskStatus(self,id,status):
        for item in self.items:
            if item.id==id:
                item.status=status
                break

def valid_input():

    valid_input = False
    while not valid_input:
        try:
            a = int(input("Enter a number between 1 to 6: "))
            valid_input = True
        except ValueError:
            print("Invalid Input. ")
    return a

def valid_input_id(str):
    valid_input = False
    while not valid_input:
        try:
            a = int(input(str))
            valid_input = True
        except ValueError:
            print("Invalid Input.")
    return a

def valid_status():
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

    todo_list.add_item(task1)
    todo_list.add_item(task2)

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

    select_input=valid_input()
    print("-" * 40)

    if select_input==1:
        a=0
        while(a!=-1):

            id=valid_input_id("Enter the id: ")
            print("Enter the task name: ")
            task = input()
            # print("Enter the Status: ")
            status=valid_status()
            item=Item(id,task,status)
            todo_list.items.append(item)
            print("Do you want to add more items y/n ")
            check=input()
            a = 0 if check == "y" else -1
        print("Tasks in ToDoList")
        todo_list.display_list()



    if select_input==2:
        print("Tasks in ToDoList")
        todo_list.display_list()

    if select_input==3:
        id=valid_input_id("Enter the id of the task you want to remove")
        todo_list.remeove_item(id)
        print("Tasks in ToDoList")
        todo_list.display_list()

    if select_input==4:
        id=valid_input_id("Enter the id of the task you want to update the name")
        print("Enter the Name you have to update")
        name=input()
        todo_list.update_item_taskName(id,name)
        print("Tasks in ToDoList")
        todo_list.display_list()

    if select_input==5:
        id=valid_input_id("Enter the id of the task you want to update the status")
        print("Enter the status you have to update")
        status=valid_status()
        todo_list.update_item_taskStatus(id,status)
        print("Tasks in ToDoList")
        todo_list.display_list()

    if select_input==6:
        execute=6