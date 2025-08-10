from googlesearch import search
from colorama import Fore, Style, init
import time

init(autoreset=True)

print(Fore.GREEN + '''



_________ _______  _______  _______  _        _        _______  _______ _________
\__   __/(  ____ \(  ____ \(  ____ \( \      ( \      (  ___  )(  ____ \\__   __/
   ) (   | (    \/| (    \/| (    \/| (      | (      | (   ) || (    \/   ) (   
   | |   | (__    | (__    | (__    | |      | |      | |   | || (_____    | |   
   | |   |  __)   |  __)   |  __)   | |      | |      | |   | |(_____  )   | |   
   | |   | (      | (      | (      | |      | |      | |   | |      ) |   | |   
___) (___| )      | (____/\| (____/\| (____/\| (____/\| (___) |/\____) |   | |   
\_______/|/       (_______/(_______/(_______/(_______/(_______)\_______)   )_(   



''')

time.sleep(2)



query = input(Fore.RED + "What you want to search: ")

print(Fore.YELLOW + "Searching for: " + query)

choose_num = input(Fore.YELLOW + "How many results do you want to see? (default is 20): ")

try:
    results = search(query, num_results=int(choose_num) if choose_num.isdigit() else 20)
    print(Fore.CYAN + "Search Results:")
    for i, result in enumerate(results, start=1):
        print(Fore.BLUE + f"{i}. {result}")
except Exception as e:
    print(Fore.RED + "An error occurred while searching: " + str(e))

print(Style.RESET_ALL + "Thank you for using this script!")
print(Fore.GREEN + "Goodbye!")
time.sleep(2)
exit()
# End of ifeellost.py