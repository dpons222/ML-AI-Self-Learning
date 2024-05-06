from modules import *

# Main program
to_do_list = []
sorted_categories_list = [sorted(categories)]

while True:
    print("\nWhat would you like to do?")
    print("1. Add Task")
    print("2. Search for Tasks by Category")
    print("3. View all Categories")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. View All Tasks")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        category = input("Enter task category: ")
        add_task(to_do_list,title, description, category)
    elif choice == "2":
        category = input("Enter category to view tasks: ")
        view_tasks_by_category(to_do_list, category)
    elif choice == "3" :
        print(sorted_categories_list)
        #for category in categories :
            #print(category)
        category_choice = input("Choose a category: ")
        if category_choice in sorted_categories_list :
            print("Category found.")
        else :
            print("Category not found.")
    elif choice == "4":
        title = input("Enter title of task to mark as completed: ")
        mark_task_as_completed(to_do_list, title)
    elif choice == "5":
        title = input("Enter title of task to delete: ")
        delete_task(to_do_list, title)
    elif choice == "6":
        print("All tasks:")
        for task in to_do_list:
            print(task)
    elif choice == "7":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")