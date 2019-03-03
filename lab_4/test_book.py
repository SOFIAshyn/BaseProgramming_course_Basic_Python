# def add_digits(num):
#     if num > 0:
#         sum = 0
#         for i in range(num - 1):
#             sum += num % 10
#             num = num // 10
#         return sum
#     else:
#         return("ERROR")
#
# print(add_digits(124))

# def nice_hello():
#     s = 'Hello, World!'
#     new_s = ''
#     for i in s:
#         new_s += s[i] + '\n'
#
#     return new_s
#
# nice_hello()

# def nice_hello():
#     s = 'Hello, World!'
#     new_s = ''
#     for c in range(len(s)):
#         new_s = i + new_s
#
#     return new_list
#
# nice_hello()

# a = 1
#
# def f():
#     if 'a' in dir():
#         return a
#     else:
#         return 10
#
# print(f())

# def change(x):
#     x = (2016, 2016)
#
# x = (2015, 2016)
# change(x)
# print(x)

# def is_positive(x):
#     print("False!")
#     return x > 0
#     print("True!")
#
# is_positive(-3)

# def change(s):
#     s = 'Hello, ' + s
#
# s = 'Andrew'
# change(s)
# print(s)

# def is_positive(x):
#     print("False!")
#     return x > 0
#     print("True!")
#
# is_positive(3)
#
# def change(lst):
#     lst.append(2016)
#
# lst = [2014, 2015]
# change(lst)
# print(lst)

# def onesDigit(n):
#     return n % 10
#
# def testOnesDigit():
#     print("Testing onesDigit()...", end="")
#     assert(onesDigit(5) == 5)
#     assert(onesDigit(123) == 3)
#     assert(onesDigit(100) == 0)
#     assert(onesDigit(999) == 9)
#     #assert(onesDigit(-123) == 3) # Буде викликати AssertionError
#     print("Passed!")
#
# testOnesDigit()

# def nice_hello():
#     s = 'Hello, World!'
#     new_s = ''
#     for i in s:
#         new_s += s[i] + '\n'
#
#     return new_s
#
# nice_hello()

# def hello_world!():
#     s = 'Hello, World!'
#     new_s = ''
#     for c in s:
#         new_s = c + new_s
#
#     return new_s
#
# hello_world!()

# line = "55"
# Line = "55"
# line = "Line"
# print(Line)

#my_d = dict(a =8, b = 9)
# for i in my_d:
#     print (i)
# for i, k in my_d.items():
#     print (i)
#     print(i, k)
#     print(k)

# def f(**kwargs):
#     names = ("a", "b")
#     res = 1
#     for k, v in kwargs.items():
#         if k in  names:
#             res *= v
#     return res
#
# my_dict = {"a": 6, "b": 7, "c": 9}
#
# print (f(**my_dict))

#import doctest
#doctest.testmod()
# assert
#

#################
# file = open('surname.txt', 'w')
# file.write("This is a test")
#
# file.close()
###################

###################
# with open ('surname.txt', 'w') as file:
#     file.write("bye!!!")
###################

my_list = [1, 2, 5, 4, 4]

new_list1 = list(filter(lambda x: x % 2 == 0, my_list))
new_list = list(map(lambda x: x ** 2, my_list))

print(new_list1, new_list)
