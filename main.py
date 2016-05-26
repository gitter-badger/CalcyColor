#<startsettings>
import help
import calcy
import calcym
import colorama
colorama.init()
#</startsettings>
#<main>#
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
    calcy.calcy()
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
        calcy.calcy()
#</main>#
