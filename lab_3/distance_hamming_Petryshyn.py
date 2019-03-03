def lenght_h():
    while True:
        try:
            num1 = int(input())
            num2 = int(input())
            break
        except ValueError:
            print("ERROR: try enter integer...")
            continue

    num3 = num1 ^ num2

    num_of_one = 0
    for i in range(8):
        if ((num3 >> i) &1) == 1:
            num_of_one += 1
    print ("Lenght Hemmigton number = ", num_of_one)


lenght_h()
