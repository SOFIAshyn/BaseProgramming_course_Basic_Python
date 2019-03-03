import urllib.request

def read_input_file(url, number):
    """
    (str, int) -> (list(list))
    Preconditions: 0 <= number <= 77

    Return list of strings lists from url

    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', '197.152', '11.60'], ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """

    import ssl


    context = ssl._create_unverified_context()

    student_lst_f = []
    student_lst_s = []
    res_lst = []
    fin_lst = []
    with urllib.request.urlopen(url,context=context) as webpage:
        for i, line in enumerate(webpage.readlines()[2:]):
            line = line.decode()
            line = line.strip()
            line = line.split()
            if len(line) == 13:
                student_lst_f.append(line)
            if len(line) == 6:
                student_lst_s.append(line)
        for i in range(len(student_lst_f)):
            student_lst_f[i][1] += " " + student_lst_f[i][2] + " " + student_lst_f[i][3]
        # print(student_lst_f)
        # print(student_lst_s)
        for j in range(number):
            res_lst = []
            res_lst.append(student_lst_f[j][0])
            res_lst.append(student_lst_f[j][1])
            res_lst.append("+")
            res_lst.append(student_lst_f[j][6])
            res_lst.append(student_lst_s[j][5])
            fin_lst.append(res_lst)
        return(fin_lst)


def write_csv_file(url):
    """
    string -> None

    Print list of sudents to csw file
    """
    str1 = ""
    url = 'https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt'
    stud_lst = read_input_file(url, 77)
    for each in stud_lst:
        str1 += ','.join(map(str, each))
        if each != stud_lst[-1]:
            str1 += "\n"
    with open('total.csv', 'w+', encoding='utf-8')  as csw_file:
        csw_file.write("№,ПІБ,Д,Заг.бал,С.б.док.осв.\n")
        csw_file.write(str1)
