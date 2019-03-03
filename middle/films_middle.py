import collections

def read_file(path):
    file = open(path, "r")

    data = set()
    for line in file:
        if line.endswith("genres\n") == False:
            data.add(tuple(line.strip().split('\t')))
            print("sfdghjkl;")
        else:
            print("poiuytr")

    file.close()
    return data


def dirctors_dict(lines_set):
    dict = {}
    for line in lines_set:
        if line[0] not in dict:
            dict[line[0]] = line[2]
    return(dict)


def add_to_file(dict):
    file = open("text.txt", "a")
    for key, el in dict.items():
        file.write(key + '\t' + el + '\n')

    file.close()

if __name__ == "__main__":
    a = read_file("title2.basics.tsv")
    # print(read_file("title2.basics.tsv"))
    print(dirctors_dict(a))
    add_to_file(dirctors_dict(a))