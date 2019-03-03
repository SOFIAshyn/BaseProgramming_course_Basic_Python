def is_power_of_two(val):
    """
    (int) -> bool

    Determine if a number is a power of two.

    >>> is_power_of_two([0])

    >>> is_power_of_two("0")

    >>> is_power_of_two(0)
    False
    >>> is_power_of_two(1)
    True
    >>> is_power_of_two(2)
    True
    >>> is_power_of_two(15)
    False
    >>> is_power_of_two(16)
    True
    """
    try:
        if val > 0 and val % 2 == 0 or val == 1:
            while val != 2:
                if val % 2 == 0:
                    val /= 2
                else:
                    break
            if val == 2 or val == 1:
                return True
            else:
                return False
        else:
            return False
    except TypeError as err:
        return None


print(is_power_of_two(24))
#
#
# def has_unique_chars(string):
#     """
#     (str) -> bool
#
#     An algorithm to determine if a string has all unique characters.
#
#     >>> has_unique_chars(None)
#     False
#     >>> has_unique_chars('')
#     True
#     >>> has_unique_chars('foo')
#     False
#     >>> has_unique_chars('bar')
#     True
#     """
#     if type(string) == str:
#         for letter in string:
#             if string.count(letter) > 1:
#                 return False
#         return True
#     else:
#         return False
#
# print(has_unique_chars("foo"))
#
# def compress(string):
#     """
#     (str) -> str
#
#     Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'.
#     Only compress the string if it saves space.
#
#     >>> compress(None)
#
#     >>> compress('')
#     ''
#     >>> compress('AABBCC')
#     'AABBCC'
#     >>> compress('AAABCCDDDDE')
#     'A3BC2D4E'
#     >>> compress('BAAACCDDDD')
#     'BA3C2D4'
#     >>> compress('AAABAACCDDDD')
#     'A3BA2C2D4'
#     """
#     if type(string) == str:
#         prev = ""
#         count = 1
#         new_str = ""
#         for letter in string + " ":
#             if letter == prev:
#                 count += 1
#             else:
#                 if count != 1:
#                     new_str += prev + str(count)
#                 else:
#                     new_str += prev
#                 count = 1
#             prev = letter
#         if len(new_str) == len(string):
#             new_str = string
#         return new_str
#     else:
#         return None
#
# print(compress(None))
#
#
import doctest
doctest.testmod()
