number = int(input("What is the range ?"))
for x in range(number):
    if x % 2 == 0:
        print(x, " an even number ")
    else:
        print(x, " an odd number ")
