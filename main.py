 
tasks = []

task = input("Enter a task: ").strip()

if task:
    tasks.append(task)
    print("Task added successfully!")
    print("Your tasks:", tasks)
else:
    print("Task cannot be empty.")