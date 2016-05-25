from termcolor import colored

print (colored("Calcy 1.0","blue"))
print (colored("Type 'help' to view a list of commands.","blue"))
user_data = raw_input(colored("$>> ", "cyan"))
if user_data == "help":
    help.help()
if user_data == "add":
    a = (colored("Type a value here: ", "magenta"))
    b = (colored("Type a value here: ", "magenta"))
    c = a + b
    d = str(c)
    a = (colored((d), "green"))
if user_data == "exit":
    print (colored("Exiting...", "red"))
    exit()
else:
    print (colored("Error: Wrong command", "red"))
    calcy.calcy()
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
        print (colored("Exiting...", "red"))
        exit()
    else:
        print (colored("Error: Wrong command", "red"))
        calcy.calcy()
