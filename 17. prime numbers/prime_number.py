def prime(n):
    its_prime = True
    for i in range(2, n):
        if n % i == 0:
            its_prime = False
    if its_prime:
        print("it is a prime number")
    else:
        print("not a prime number")

    
prime(7)