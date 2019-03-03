import sys

def consol(lst):
    _argc = len(lst)
    print(_argc, lst)


def from_file(name_f):
    file = open(name_f, "r")
    lst = [i.split() for i in file]
    a = []
    a.extend(lst[0])
    print (lst)
    a, b , c = (lambda x: x for x in lst)
    print(a, b, c)

if __name__ == "__main__":
    consol(sys.argv)
    from_file('squerance.txt')