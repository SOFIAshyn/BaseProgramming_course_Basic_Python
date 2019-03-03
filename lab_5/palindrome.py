def isPalindrome(s):

    def isChar(s):
        s = s.lower()
        letters = ""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                letters += c
        return letters

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(isChar(s))

print(isPalindrome("anna"))
