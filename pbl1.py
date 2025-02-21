import json

def load_todos():
    try:
        with open("todos.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"todos":[]}

def save_todos(todos):
    datas = {"todos": todos}
    with open("todos.json","w") as file:
        json.dump(datas, file)
        
def list_menu():
    menu=("Add todo","Update todo","Show todo","Delete todos","Reset todos","exit program")
    for i,v in enumerate(menu,1):
        print(f"{i}. {v}")

#Create
def add_todos(todos):
    while True:
        todo = input("Enter your todo(or Exit): ")
        if todo == "exit":
            break
        else:
            todos.append(todo)
    return todos

#Update
def update_todos(todos):
    while True:
        try:
            choose = int(input("Choose your todo(0 for exit): "))
            print(f"Your todo is {todos[choose-1]}")
            if choose == 0 :
                break
            elif choose > 0:
                todos[choose-1] = input("Update your todo: ")
            else:
                print("Out of Range")
        except ValueError:
            print("Invalid Input")
    return todos

#showtodos
def show_todos(todos):
    if len(todos) >= 0:
        for i,v in enumerate(todos,1):
            print(f"{i}. {v}")
    else:
        print("Your todos is empty")

# Delete
def delete_todos(todos):
    while True:
        choose_index = int(input("Choose your todo (or 0 for exit): "))
        if choose_index == 0:
            break
        todos.pop(choose_index-1)
    return todos

# clearall
def delete_all_todos(todos):
    confirm = input("Are you sure want to clear all todos? Y/N: ").upper()
    if confirm == "Y":
        todos.clear()
    elif confirm =="N":
        print("Canceled")
        return todos

if __name__ == "__main__":
    todos = load_todos()
    todos_todos = todos["todos"]
    print("Welcome to out todo app aplication")
    while True:
        list_menu()
        choose_menu = int(input("Enter the menu: "))
        match choose_menu:
            case 1:
                todos = add_todos(todos_todos)
                save_todos(todos)
            case 2:
                todos = update_todos(todos_todos)
                save_todos(todos)
            case 3:
                print("#####################")
                show_todos(todos_todos)
                print("#####################")
            case 4:
                todos= delete_todos(todos)
            case 5:
                todos = delete_all_todos(todos)
            case 6:
                confirm = input("Are you sure want to quit program? (Y/N)").upper()
                if confirm == "Y":
                    exit()
                elif confirm == "N":
                    break
                else:
                    print("nothing todo invalid input")
    