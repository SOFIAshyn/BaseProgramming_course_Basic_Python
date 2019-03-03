s = 'abcD'
t = 'cd'

def isLowerCase(s):
    aCode = ord('a')
    zCode = ord('z')

    for item in s:
        code = ord(item)
        if (code < aCode or code > zCode):
            return False
        return True

def isPalindrom(s):
    for i in range(len(s) // 2):
        if (s[i]) != (s[-1 - i]):
            return Flase
        return True

cap = s.capitalize()
coun = s.count("a")
endline = s.endswith("wd");

def my_edswith(s, t):
    if (len(t) > len(s)):
        return False
    for i in range(len(t)):
        if (s[-1 - i]) != (t[-1 - i]):
            return False
    return True

def milk_pie():
    n = int(input())
    students = list(input().stip().split(" "))

    cnt = 0

    for item in students:
        if (item < 30):
            cnt += 1

    pie_num = cnt
    neededMilk = cnt * 200
    capacity = 900

    bagsOfMilk = need // capacity
    if (need % cap != 0):
        bags += 1

    print( bags, numpie)
