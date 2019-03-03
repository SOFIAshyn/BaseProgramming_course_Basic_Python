def product():
    n = int(input())
    dob = 1
    if n > 0:
        for i in range(1, n+1):
            if i % 7 != 0:
                dob *= i
        return dob

print(product())
