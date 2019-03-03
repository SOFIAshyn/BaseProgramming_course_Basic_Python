import math

def Leibniz_Gregory_Madhava(n):
    count = 0
    my_pi = 0
    s = 1
    for i in range(1 ,n * 2, 2):
        count += 1
        my_pi = my_pi + s * (4 / i)
        s = (-1) * s
    return my_pi, count

def Arhimed():
    # max error allowed
    eps = 1e-10

    # initialize w/ square
    x = 4
    y = 2*math.sqrt(2)

    count = 0
    while round(x-y) == round(math.pi):
        x1 = 2*x*y / (x + y)
        y    = math.sqrt(x1 * y)
        x    = x1w
        count += 1
    my_pi = str((x + y)/ 2)
    return my_pi, count

    print("PI = " + str((x+y)/2))
    print("# of iterations = " + str(ctr))

def Chudn():
    t = 1 / 4
    a = 1
    b = 1 / math.sqrt(2)
    p = 1
    count = 0

    while a != b:
        count += 1
        a_p = a
        my_pi = (a + b)** 2 / (4 * t)
        a = (a + b) / 2
        b = math.sqrt(a * b)
        t = t - (p * ((a_p - a)** 2))
        p = 2 * p
    return my_pi, count

n = int(input())

if n < 9 and n > 0:
    norm_pi = math.pi

    new_pi, count = Leibniz_Gregory_Madhava(n)
    dif = norm_pi - new_pi
    print("Leibniz_Gregory_Madhava: ")
    print("Our pi: ", new_pi)
    print("Number of Iterations: ", count)
    print("Difference:", dif, "\n")

    new_pi, count = Chudn()
    dif = norm_pi - new_pi
    print("Chudnovki: ")
    print("Our pi: ", new_pi)
    print("Number of Iterations: ", count)
    print("Difference:", dif, "\n")

    new_pi, count = Arhimed()
    dif = norm_pi - float(new_pi)
    print("Arihmed: ")
    print("Our pi: ", new_pi)
    print("Number of Iterations: ", count)
    print("Difference:", dif, "\n")

else:
    ValueError
