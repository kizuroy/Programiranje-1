def collatzova_domneva():
    n = int(input("Vnesi število: "))
    while n != 1:
        print(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    print(1)

collatzova_domneva()