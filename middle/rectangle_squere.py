import math

a, b, c = 10, 10, 12

h = int(pow(a * a - (b * b) / 4, 1/2))

x = (h * c)/(c + h)

print(x)
