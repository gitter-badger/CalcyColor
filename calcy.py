import colorama
import help
import calcym
colorama.init()
def calcy():
    cmd = input(colorama.Fore.CYAN + "$>> " + colorama.Fore.RESET)
    if cmd == "help":
        help.help()
    elif cmd == "add":
        a = (colorama.Fore.GREEN + "Type a number: " + colorama.Fore.RESET)
        b = (colorama.Fore.GREEN + "Type a number: " + colorama.Fore.RESET)
        d = calcym.add(a,b)
        e = str(d)
        print (e)
    else:
        print (colorama.Fore.RED + "ERROR: WRONG COMMAND" + colorama.Fore.RESET)
        print (colorama.Fore.RED + "RUNTIME ERROR" + colorama.Fore.RESET)
    while cmd == "add" or "help":
        print (colorama.Fore.MAGENTA + "CALCY 1.0" + colorama.Fore.RESET)
        print (colorama.Fore.MAGENTA + "Type 'help' to view a list of commands." + colorama.Fore.RESET)
        cmd = input(colorama.Fore.CYAN + "$>> " + colorama.Fore.RESET)
        if cmd == "help":
            help.help()
        elif cmd == "add":
            a = (colorama.Fore.GREEN + "Type a number: " + colorama.Fore.RESET)
            b = (colorama.Fore.GREEN + "Type a number: " + colorama.Fore.RESET)
            d = calcym.add(a,b)
            e = str(d)
            print (e)
        else:
            print (colorama.Fore.RED + "ERROR: WRONG COMMAND" + colorama.Fore.RESET)
            print (colorama.Fore.RED + "RUNTIME ERROR" + colorama.Fore.RESET)
