to_do_list=[]
def show_menu():
    print("Menu choices for to-do-list")
    print("1. Add task")
    print("2. Mark task as completed(remove it)")
    print("3. Sort task alphabetically")
    print("4. Edit task")
    print("5. Exit")
while True:
    show_menu()
    choice = input("Enter  your choice (1-5):")
    if choice=="1":
        task=input("Enter task to add in list: ")
        to_do_list.append(task)
        print("Task is added to to-do-list successfully. Here is your updated to-do-list :",  to_do_list)
    elif choice=="2":
        if to_do_list:
            completed_task=input("Enter the  task you completed: ")
            if completed_task in to_do_list:
                to_do_list.remove(completed_task)
                print(f"Task '{completed_task}' removed. Here is your updated to-do-list:  ",to_do_list)
            else:
                print(f"'{completed_task}' does not exist in to-do list.")
        else:
            print("List is empty nothing to remove.")
    elif choice=="3":
        if to_do_list:
            to_do_list.sort()
            print("Todo list sorted. Here is your updated to-do-list: ", to_do_list)
    
        else:
            print("Todo list is empty nothing to sort.")
    elif choice=="4":
        if to_do_list:
            old_item=input("Enter task you want to edit: ")
            
            if old_item in to_do_list:
                new_item=input("Enter new value you want to replace with:")
                for i in range(len(to_do_list)):
                    if to_do_list[i]==old_item:
                        to_do_list[i]=new_item
                print("your task is updated. Here is your updated to-do-list :", to_do_list)
            else:
                print(f"'{old_item}' does not exist in list.")
        else:
            print("ToDo list is empty nothing to edit.")
    elif choice=="5":
        print("Exiting the to-do-list.....")
        break
    else:
        print("Wrong choice please enter choices from (1-5):")
                    
