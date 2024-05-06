categories = set()
# Function to add a task to the to-do list
def add_task(to_do_list,title, description, category):
    global categories
    global sorted_categories_list
    task = (title, description, category)
    to_do_list.append(task)
    categories.add(category)
    sorted_categories_list = sorted(categories)
    print("Task added successfully.")

# Function to view tasks by category
def view_tasks_by_category(to_do_list, category):
    print(f"Tasks in category '{category}':")
    for task in to_do_list:
        if task[2] == category:
            print(task[0])

# Function to mark a task as completed
def mark_task_as_completed(to_do_list, title):
    for task in to_do_list:
        if task[0] == title:
            to_do_list.remove(task)
            print("Task marked as completed.")
            return
    print("Task not found.")

# Function to delete a task
def delete_task(to_do_list, title):
    for task in to_do_list:
        if task[0] == title:
            to_do_list.remove(task)
            print("Task deleted.")
            return
    print("Task not found.")

    # Function to extract category set
    def extract_category(to_do_list) :
        categories = set()
        for task in to_do_list :
            categories.add(task[2])
        return sorted(categories)

