def isprime(k):
    for item in range(3, k):
        if k % item == 0:
            return False
            break
        else:
            return True

num = input()
if (num.isdigit() == False) or (int(num) > 2):
    num = int(num)
    for i in range(3, num):
        if isprime(i):
            if num % i != 0:
                print (i)
                break
else:
    print ("Error")
