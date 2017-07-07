import  sys
import requests
import json
print("Welcome to the Horus Manager app!")

def get_users():
    global user
    user = input("User:")
    global  passw
    passw = input("Password:")

def execute_shell():
    print("Type the command you want to execute or type 'help' if you`re lost")
    while True:
        inp = input(">>>")
        inp = inp.lower()
        Actions_description = ["Add: add an item to the database", "Remove: delete an item from the database ",
                        "View: see information about an item", "Exit: exit shell"]

        Action_list = ["add", "remove", "exit", "view", "help"]
        if inp == "help":
            print("The actions are: ")
            for action in Actions_description:
                print(action)
        elif inp not in Action_list and inp != "":
            print("Not a valid command.")
        elif inp == "exit":
            sys.exit()
        elif inp == "add":
            add()
        elif inp == "remove":
            remove()
def add():
    tok = 0
    actions_add = ("battery", "computer", "rope", "charger")
    print("What do you want to add?... type 'options' to see what you can add or type 'back' to go back to the Horus Manager App Shell")
    while tok == 0:
        prmt = input(">>>")
        prmt = prmt.lower()
        if prmt == "options":
            for action_2 in actions_add:
                print(action_2)
        elif prmt == "battery":
            comment = input("Agrega la información: ")
            battery_number = input("Which battery is it? ")
            try:
                battery_number = int(battery_number)
            except ValueError:
                print("Not a valid number")
            data = {'data_fields': comment, 'name': 'Number ' + str(battery_number), 'type': 'battery', 'user': user}
            r = requests.post('http://192.168.0.1:5000/create', json= data)
            response = r.json()
            id = response['id']
            print("Tu entrada se guardo en la id: " + str(id))
            tok += 1
        elif prmt == "computer":
            print("Aqui agregas la informacion de la computadora")
            tok += 1
        elif prmt == "rope":
            print("Aqui agregas la informacion de la cuerda")
            tok += 1
        elif prmt == "charger":
            print("Aqui agregas la informacion del cargador")
            tok += 1
        elif prmt == "back":
            tok += 1
            pass
        elif prmt != "" and prmt not in actions_add:
            print("Not a valid command.")

def remove():
    tok = 0
    actions_rem = ("battery", "computer", "rope", "charger")
    print(
        "What do you want to remove?... type 'options' to see what you can delete or type 'back' to go back to the Horus Manager App Shell")
    while tok == 0:
        prmt = input(">>>")
        prmt = prmt.lower()
        if prmt == "options":
            for action_2 in actions_rem:
                print(action_2)
        elif prmt == "battery":
            print("Aqui agregas la informacion de la bateria")
            tok += 1
        elif prmt == "computer":
            print("Aqui agregas la informacion de la computadora")
            tok += 1
        elif prmt == "rope":
            print("Aqui agregas la informacion de la cuerda")
            tok += 1
        elif prmt == "charger":
            print("Aqui agregas la informacion del cargador")
            tok += 1
        elif prmt == "back":
            tok += 1
            pass
        elif prmt != "" and prmt not in actions_rem:
            print("Not a valid command.")

usuarios = ("HORUS", "emi", "paok", "fish")
contraseñas = ("root", "a00344591", "12345", "67890")

def validar_usuario():
    if user in usuarios and passw in contraseñas:
        us_pos = usuarios.index(user)
        pss_pos = contraseñas.index(passw)
        if us_pos == pss_pos:
            return True
        else:
            return False
    else:
        return False

def check():
    x_count = 0
    while x_count < 3:
        get_users()
        if validar_usuario():
            execute_shell()
        elif x_count < 1:
            x_count += 1
            print("Error de usuario... Vuelve a intentar...")
            print("Te quedan " + str(3 - x_count) + " intentos")
        elif x_count < 2:
            x_count += 1
            print("Error de usuario... Vuelve a intentar...")
            print("Te queda " + str(3 - x_count) + " intento")
        else:
            x_count += 1
            print("Ha introducido varios usuarios y/o contraseñas erroneas... SALIENDO DEL PROGRAMA...")

check()
