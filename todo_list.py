tasks = []

def add(task):
    tasks.append(task)

def view():
    for idx, task in enumerate(tasks,1):
        print(f"{idx}.{task}")

def delete (index):
    try:
        tasks.pop(index-1)
    except IndexError:
        print("invalid task number")

while True:
    print("\n1.Add Task\n2.view task\n3.delete")
    choice = input("enter a number: ")

    if choice == '1':
        task = input("enter task: ")
        add(task)
    elif choice == '2':
        view()
    elif choice == '3':
        view()
        task_idx =int(input("enter task number to delete: "))
        delete(task_idx)
    else:
        print("invalid choice")
