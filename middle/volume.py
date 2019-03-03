import math

def user_input():
    r = int(input("Radius = "))
    h = int(input("Height: "))
    accuracy = int(input("Accuracy: "))
    return r, h, accuracy

def volume(r, h):
    cylinder = math.pi * r ** 2 * h
    print(cylinder)
    hemisphere = (2.0 / 3.0) * math.pi * r**3
    print(2.0 / 3.0)
    print(math.pi)
    print(r**3)
    print(hemisphere)
    conus = (1.0/3.0) * math.pi * r**2
    print(conus)
    return cylinder/hemisphere/conus, hemisphere/conus/cylinder, conus/cylinder/hemisphere

def main():
    r, h, accuracy = user_input()
    input3 = volume(r, h)
    for i, el in enumerate(input3):
        # print(i + 1, ' = %.8f' % el)
        print(i + 1, (' = %.' + str(accuracy) + 'f') % el)
        # print(i + 1, ' = %.6f' % el)

main()