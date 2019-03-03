with open ("text.txt", "w") as f:
    f.write("Hello")

with open ("text.txt", "r") as f:
    for line in f:
        print(line)
