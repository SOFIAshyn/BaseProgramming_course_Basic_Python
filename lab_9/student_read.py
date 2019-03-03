def num_average(lst):
    """
    (list) -> int
    """
    return round(sum(lst)/len(lst), 3)


def read_file():
    student_dict = {}
    first_line = ""
    with open("student.txt", "r") as f:
        for line in f.readlines():
            if line.startswith("Subject"):
                if line.startswith("Student"):
                    first_line = line
                if line.split()[0] not in student_dict.keys():
                    name = ""
                    name = name.join(line.split()[:2])
                    marks = line.strip().split()
                    marks = list(filter\
                            (lambda num: num.isdigit(), marks))[1:]
                    marks = list(map(int, marks))
                    student_dict[name] = marks
    for stud in student_dict.keys():
        student_dict[stud].append([num_average(marks)])
        # student_dict[stud][1] = num_average(marks)
        #marks.insert(0, first_line)
    print(student_dict, end="")

read_file()
