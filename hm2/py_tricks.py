def fun(x, y, z):
    print(x, y, z)

tpl = (1, 0, 4)
dct = {"1": 1, "2": 0, "3": 4}

fun(*tpl)
fun(**dct)
