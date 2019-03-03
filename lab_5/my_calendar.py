import calendar

count = 0
for i in range(2000, 2051):
    if calendar.isleap(i):
        count += 1
print(count)

print(calendar.isleap(2016))

