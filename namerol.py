
import random


names = input("Give me the list of names seperated by a comma")


namelist = names.split(",")

items = len(namelist)

#randnames = random.randint(0, items-1)

#chosen = namelist[randnames]

chosen = random.choice(namelist)

print(chosen + " " + "is paying for the damn check!")