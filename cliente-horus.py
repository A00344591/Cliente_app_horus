print("Welcome to the Horus Manager app!")

def users():
    global user
    user = input("User:")
    global  passw
    passw = input("Password:")

def execute_shell():
    print("Type the command you want to execute or type 'help' if you lost")
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
def users2():
    x_count = 0
    while x_count < 3:
        users()
        if user == "HORUS6348" and passw == "double_sided_tape":
            execute_shell()
        else:
            x_count += 1
            print("Error de usuario... Vuelve a intentar...")
            print("Te quedan " +str( 3-x_count ) + " intentos")

users2()