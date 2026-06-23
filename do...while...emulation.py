while True:
    n1 = int(input("Enter number 1st: "))
    n2 = int(input("Enter number 2nd: "))
    print("Sum of two numbers is: ", n1 + n2)

    check = input("Do you want to continue...? (y/n): ")

    if check.lower() != 'y' or check.upper() != 'Y':
        break