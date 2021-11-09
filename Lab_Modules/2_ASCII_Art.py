from pyfiglet import figlet_format
from termcolor import colored
word = figlet_format("Alina", font="isometric1")
print(colored(word, "yellow", attrs=['bold']))