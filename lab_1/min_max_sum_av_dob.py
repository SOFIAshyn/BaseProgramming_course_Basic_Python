num = int(input("Number: "))
list1 = []
sum = 0
dob = 1

for i in range(num):
    t = int(input())
    list1.append(t)

min = list1[0]
max = list1[0]

for i in range(num):
    if min > list1[i]:
        min = list1[i]
    if max < list1[i]:
        max = list1[i]
    #print (list1.min())
    sum += list1[i]
    dob *= list1[i]
av = float(sum)/num
print ("min: " , min, "max: ", max , "av: ", av ,"sum: ", sum , "dob: ", dob)
