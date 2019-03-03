import student_read

if __name__ == "__main__":
    try:
        n = int(input("Name of student: "))
    except ValueError as err:
        print("You have made a great misstake", err)
    student_read.average_mark()
