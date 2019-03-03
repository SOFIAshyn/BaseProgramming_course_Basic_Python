def weight_h():
    Evil = []
    Odious = []
    for x in range(0, 21):
        num_of_one = 0
        num = 5 **x
        s_num = str(bin(num))
        for i in range(len(s_num) - 2):
            if (num >> i & 1) == 1:
                num_of_one += 1
        print ("Weight Hemmigton of number 5 ** ", x , " = ", num_of_one)
        if num_of_one % 2 == 0:
            Evil.append(num)
        else:
            Odious.append(num)
    print ("Evil numbers = ", Evil)
    print ("Odious numbers = ", Odious)

weight_h()
