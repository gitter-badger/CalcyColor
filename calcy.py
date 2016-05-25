from termcolor import colored

import help

def calcy():
    user_data = raw_input(colored("$>> ", "cyan"))
    if user_data == "help":
        help.help()
    elif user_data == "add":
        a = (colored("Type a value here: ", "magenta"))
        b = (colored("Type a value here: ", "magenta"))
        c = a + b
        d = str(c)
        a = (colored((d), "green"))
    elif user_data == "exit":
        print (colored("Exiting...", "yellow"))
        exit()
    else:
        print (colored("Error: Wrong command", "red"))
        print (colored("Runtime crashed! Exiting...", "red"))
        exit()
    while user_data == "add" or user_data == "help":
        user_data = raw_input(colored("$>> ", "cyan"))
        if user_data == "help":
            help.help()
        elif user_data == "add":
            a = (colored("Type a value here: ", "magenta"))
            b = (colored("Type a value here: ", "magenta"))
            c = a + b
            d = str(c)
            a = (colored((d), "green"))
        elif user_data == "exit":
            print (colored("Exiting...", "yellow"))
            exit()
        else:
            print (colored("Error: Wrong command", "red"))
            print (colored("Runtime crashed! Exiting...", "red"))
            exit()
