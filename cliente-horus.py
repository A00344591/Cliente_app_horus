#import requests

inp = ""

while True:
    inp = input(">>>")

    if inp == "Display commands":

        Actions_list = ["Add", "Remove", "View"]
        for action in Actions_list:
            print(action)

