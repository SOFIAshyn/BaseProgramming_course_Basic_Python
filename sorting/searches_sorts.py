import all_searches, all_sorts


def enterList():
    user_lst = []
    user_number = input("Write a number: ")
    while user_number != '\n':
        user_lst.append(user_number)
        user_number = input("Write a number: ")
    return user_lst


def main():
    user_lst = enterList()
    print("Now we are going to test all sorting algorithms:\n")
    all_sorts.main(user_lst)
    print("Now we are going to test all searching algorithms:\n")
    all_searches.main(user_lst)


if __name__ == "__main__":
    main()
