a = list("wahoo!")
print(a) # prints: ['w', 'a', 'h', 'o', 'o', '!']
# use "".join(a) to convert a list of characters to a single string
s = "".join(a)
print(s) # prints: wahoo!
# "".join(a) also works on a list of strings (not just single characters)
a = ["parsley", " ", "is", " ", "gharsley"] # by Ogden Nash!
s = "".join(a)
print(s) # prints: parsley is gharsley
