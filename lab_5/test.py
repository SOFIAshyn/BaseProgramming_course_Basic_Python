# def a(x):
#     print(12)
#
# def b():
#     print (x)
#
# a(5)
# b()
#
# a, b, c = 9, 4, 1
# if a > b:
#     if b > c:
#         print( "Допоможіть будь ласка!", end = " ")
#     else:
#         print( "Все було чудово!", end = " ")
# elif b > c:
#     print( "Каву будь ласка,", end = " ")
#     if a >= c:
#         print( "чорну.", end = " ")
#     elif a < b:
#         print( "з молоком.", end = " ")
#     elif c == b:
#         print( "без цукру.", end = " ")
# else:
#     print( "Чай будь ласка,", end = " ")
#     if a == b:
#         print( "з цукром.", end = " ")
#     else:
#         print( "з молоком.", end = " ")
# print( "Дякую")

a, b, c = 1, 5,1


a, b, c = 5, 7, 9
if a > b:
    if b > c:
        print( "Допоможіть будь ласка!", end = " ")
    else:
        print( "Все було чудово!", end = " ")
elif b > c:
    print( "Каву будь ласка,", end = " ")
    if a >= c:
        print( "чорну.", end = " ")
    elif a < b:
        print( "з молоком.", end = " ")
    elif c == b:
        print( "без цукру.", end = " ")
else:
    print( "Чай будь ласка,", end = " ")
    if a == b:
        print( "з цукром.", end = " ")
    else:
        print( "з молоком.", end = " ")
print( "Дякую")
