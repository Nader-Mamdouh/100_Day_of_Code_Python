import random
name = input('Give me everybody name separated by "," \n')
name = name.split(", ")
size = len(name)
randomnumber = random.randint(0, size-1)
target = name[randomnumber]
print(f"{target} will pay for all of us today")
