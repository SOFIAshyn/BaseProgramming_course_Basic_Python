def isprime(n):
    if n == 2:
        return False
    for item in range(2, n):
        if n % item == 0:
            return False
            break
    return True

num = input()

if num.isdigit():
    if int(num) > 2:
        num = int(num)
        for i in range(2, num):
            if isprime(i) == True:
                if (num % i != 0):
                    print(i)
                    break
    else:
        print("Error")
else:
    print("Error")
