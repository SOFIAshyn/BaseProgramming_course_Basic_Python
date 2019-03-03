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

    import urllib.request
    import ssl


    context = ssl._create_unverified_context()

    student_lst = []
    clear_st_lst = []
    with urllib.request.urlopen(url,context=context) as webpage:
        url = webpage.read(number)
        print(type(url))
        for line in url:
            #line = line.decode()
            line = line.replace('\t', " ")
            line = line.split()
            student_lst.append(line)
        print(student_lst)
        #clear_st_lst += student_lst[::8] + student_lst[3:][::8]

                #print(i, line)
        # for i, each_el in enumerate(student_lst[i:i+7]):
        #     if i == 0 or i == 3:
        #         clear_st_lst.append(each_el)
        #     i += 8
        #     print(clear_st_lst)



            # line = line.strip('\n')
            # line = line.split()
        # for each_line in line:
        #     for i in range(6):
        #         student += each_line
            #print(type(line.decode()))
            #line = webpage.read().decode()
        print(student_lst)

def write_csv_file(url):
    pass


print(read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt',3))
