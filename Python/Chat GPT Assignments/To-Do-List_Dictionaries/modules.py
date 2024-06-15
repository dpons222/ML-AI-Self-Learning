# Using a dictionary to store tasks
task_manager = {}

def add_task(task_manager, title, description, category):
    task = {'title': title, 'description': description, 'category': category}
    task_manager[title] = task
    print("Task added successfully.")

def view_task_by_title(task_manager, title):
    task = task_manager.get(title)
    if task:
        print("Task details:")
        for key, value in task.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("Task not found.")

