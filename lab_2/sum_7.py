def sum_7():
    sum = 0
    n = int(input())
    if n > 0:
        for i in range(1, n + 1):
            if i % 7 == 0:
                sum = sum + i
        return sum

print (sum_7())
