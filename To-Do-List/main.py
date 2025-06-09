import json

print("Welcome to To-Do List app. What you want to do\n1- Viwe Tasks \n2- Add Task \n3- Delete Task\n")

def add_task(taskName, taskDesc):
    with open("task.json", "r") as f:
        data = json.loads(f.read())

    with open("task.json", "w") as g:
        data.append({"Name":taskName, "Desc":taskDesc})
        g.write(json.dumps(data))
    print("Task Successfuly Added\n")


def viwe_task():
    with open("task.json", "r") as f:
        data = json.loads(f.read())
        print("\n----------------------- All Tasks -----------------------\n")
        for i, item in enumerate(data):
            print(i+1, "-", item["Name"], ":", item["Desc"])
        print("\n----------------------- Tasks End -----------------------\n")

def delete_task(index):
    with open("task.json", "r") as f:
        data = json.loads(f.read())

    if len(data) > index:
        with open("task.json", "w") as g:
            del data[index]
            g.write(json.dumps(data))
        print("Task Successfuly Deleted\n")
    else:
        print("pleaes Enter task number which exsits")

def main():
    while True:
        task = input("1->Viwe, 2->Add, 3->Delete 4->quit: ")

        if task == "2":
            name = input("\nWhat is Task name: ")
            description = input("what is Task Description: ")
            add_task(name, description)

        elif task == "1":
            viwe_task()

        elif task == "3":
                delete_index = int(input("\nWhich task do you want to Delete: "))
                delete_task(delete_index-1)
        
        elif task == "4":
            break

        else:
            print("\nWrong input please chose correct value 1,2,3")

if __name__ == "__main__":
    main()
