def odd_sum(n):
    res = [0]
    n = list(i for i in range(n))
    prev = 0
    add_i = 0
    for i in n:
        if i in n[1::2]:
            add_i = i + prev
            prev += i
        res.append(add_i)
    return res

print(odd_sum(4))

def fac(n):
    if n == 1:
        return n
    else:
        return n * fac(n-1)

print(fac(5))
