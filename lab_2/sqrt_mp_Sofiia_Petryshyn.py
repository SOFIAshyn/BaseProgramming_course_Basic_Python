import math

def newton_raphson(k):
    count = 0
    epsilon = 0.01
    guess = k/2.0
    while abs(guess * guess - k) >= epsilon:
        guess = guess - (((guess**2) - k)/(2*guess))
        count += 1;
    return guess, count

def binsqrt(n):
    count = 0
    sgn = 0
    if n < 0:
        n = -n
        sgn = -1
    low = 0.0
    upp = n
    mid = (low + upp) * 0.5
    while True:
        count += 1
        if mid * mid > n:
            upp = mid
        else:
            low = mid
        last = mid
        mid = (upp + low) * 0.5
        if abs(mid - last) < 1e-9:
            break
    if sgn < 0:
        return complex(0, mid)
    return mid, count

def squareroot(inputNum):
    count = 0
    if inputNum < 4:
        count += 1
        return 1, count
    else:
        halfnum = inputNum / 2
        for num in range(2, int(halfnum)):
            count += 1
            if num * num == inputNum:
                return num, count
            elif num * num < inputNum:
                continue
            else:
                return num-1, count

num = int(input())

fnc_sqrt = math.sqrt(num)

sq, count = newton_raphson(num)
dif = fnc_sqrt - sq
print("Newton-Raphson: ")
print("Squered root: ", sq)
print("Number of Iterations: ", count)
print("Difference:", dif, "\n")

sq, count = binsqrt(num)
dif = fnc_sqrt - sq
print("Binary search: ")
print("Squered root: ", sq)
print("Number of Iterations: ", count)
print("Difference:", dif, "\n")

sq, count = squareroot(num)
dif = fnc_sqrt - sq
print("Binary search: ")
print("Squered root: ", sq)
print("Number of Iterations: ", count)
print("Difference:", dif, "\n")
