def prime_number(number):
    is_prime = True
    if number < 2:
        is_prime = False
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
    if is_prime:
        print("it is a prime number ")
    else:
        print("it is not a prime number ")


number = int(input("What is the number you want to check ? "))
prime_number(number)
