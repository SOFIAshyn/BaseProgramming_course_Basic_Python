import time

#***************************************
# OPENI FILE 1
#***************************************
f = open("example.txt", encoding = "utf - 8")
# All file
content = f.read()
print(content)
# f.close()

# Every line 1
f.seek(0) # when end is reached > 0 position
start = time.time()
lines = f.readlines()
print(time.time() - start)
print(lines)
# f.close()

# Every line 2
f.seek(0)
start = time.time()
for line in f:
    print("- -", line)
print(time.time() - start)
f.close()
