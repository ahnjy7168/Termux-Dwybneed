import os
import random
from time import sleep
os.system("clear")
print("""
 ____  ____                 _   _   _             _
|  _ \|  _ \  ___  ___     / \ | |_| |_ __ _  ___| | __
| | | | | | |/ _ \/ __|   / _ \| __| __/ _` |/ __| |/ /
| |_| | |_| | (_) \__ \  / ___ \ |_| || (_| | (__|   <
|____/|____/ \___/|___/ /_/   \_\__|\__\__,_|\___|_|\_\
""")
os.system("termux-setup-storage")
os.system("pkg update")
os.system("pkg upgrade")
os.system("pkg install git")
os.system("pkg install wget")
os.system("pkg install openssh")
os.system("pkg install python")
os.system("pkg install nano")
os.system("clear")

os.system("figlet -f small Dwybneed.py")
os.system("figlet -f small dowloading")

number = random.randint(2,3)

for i in range(number):
	os.system("figlet -f small loading-")
	sleep(1)
	os.system("figlet -f small loading--")
	sleep(1)
	os.system("figlet -f small loading---")
	sleep(1)
	os.system("figlet -f small loading----")
	sleep(1)

os.system("clear")
print("Download is complte")
sleep(0.2)
print("Thank you for using our servuce.")
sleep(3)
os.system("clear")
