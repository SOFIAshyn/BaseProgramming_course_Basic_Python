# import math
#
# #import os
# #a, b, c = eval(input("Please enter the coefficients (a, b, c) : "))
# #print(os.listdir())
#
# s = input("a, b, c = ")
# a, b, c = s.split()
# a, b, c = float(a), float(b), float(c) #автоматичне присвоювання
#
# #a,b , c = map (float, input("a,b,c = ")).split()
#
# disc_root = math.sqrt(b * b - 4 * a * c)
# root1 = (-b + disc_root) / (2 * a)
# root2 = (-b - disc_root) / (2 * a)
#
# print("The roots are: ", root1, root2)
#
# print (int(4 * math.pi * (1 /  math.pi) ** 0.5) ** 2)

def isprime(k):
    for i in range(3, k):
        if k % i == 0:
            return False
        else:
            return True

n = int(input())
if (isprime(n)):
    print("yes")
else:
    print("no")
