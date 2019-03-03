plaintext = "i am cesear"
plaintext = plaintext.replace(" ", "")
k = int(input("k: "))
alphabet = "abcdefghijklmnopqrstuvwxyz"


def encryt(plaintext):
    dict = {}
    for letter_n in range(26):
        dict[alphabet[letter_n]] = letter_n
    return dict


def cryp_text(dict, key):
    res = []
    for letter in plaintext:
        res.append(dict[letter] + key)
    for el in res:
        for d_key, d_val in dict:
            if d_val == res[el]:
                res_enc.append(d_key)
    print(res_enc)
    return res


def encrypt(num_lst, dict):
    res_enc = []
    for el in range(len(num_lst)):
        num_lst[el] -= k
        for d_key, d_val in dict.items():
            if d_val == num_lst[el]:
                res_enc.append(d_key)
    return res_enc

en = encryt(plaintext)
a = cryp_text(en, k)
print(encrypt(a, en))
