import sys

k = 67
try:
    a = sys.stdin.readline()
    sys.stdout.write(a)
    print(sys.platform)
    print(sys.version)
    print(sys.getsizeof(5))
    print(sys.getdefaultencoding())
    print(sys.getrecursionlimit())
    print(sys.modules)
except TypeError:
    sys.stderr.write("It is an error\n")
    print(sys.path)
    sys.exit("dfghjk")
#print(sys.builtin_module_names)
