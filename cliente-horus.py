print("Welcome to the Horus Manager app!!!")
print("Type the command you want to execute or type 'help' if you lost")

def execute_shell():
    while True:
        inp = input(">>>")
        inp = inp.lower()
        Actions_description = ["Add: add an item to the database", "Remove: delete an item from the database ",
                        "View: see information about an item", "Exit: exit shell"]

        Action_list = ["add", "remove", "exit", "view"]
        if inp == "help":
            print("The actions are: ")
            for action in Actions_description:
                print(action)
        if inp not in Action_list and inp != "" and inp !="exit":
            print("Not a valid command.")

        if inp=="exit":
            break



execute_shell()