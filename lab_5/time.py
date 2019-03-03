import time

def prime_number_faster(num):
    if (num < 2):
        return False
    if (num == 2):
        return True
    if (num % 2 == 0):
        return False
    max_factor = round(num ** 0.5)
    print(num, "max = ", max_factor)
    for factor in range(3, max_factor + 1, 2):
        print("factor = ", factor)
        if (num % factor == 0):
            return False
    return True

def prime_number(num):
    if (num < 2):
        return False
    for factor in range(2, num):
        if (num % factor == 0):
            return False
    return True

prime_range = 1010809
print("prime_number(", prime_range,")", end=" ")
time_start = time.time()
print(", primes ", prime_number(prime_range), end=" ")
time_stop = time.time()
print(", time is ",(time_stop - time_start) * 1000,"ms")

print("prime_number_faster(",prime_range,")", end=" ")
time_start = time.time()
print(", returns ", prime_number_faster(prime_range), end=" ")
time_stop = time.time()
print(", time is ",(time_stop - time_start) * 1000,"ms")