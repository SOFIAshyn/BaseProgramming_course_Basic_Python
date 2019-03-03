from utils import process_file

text = process_file("data.txt")

words = text.split()
set_words = set(words)
print(len(words), len(set_words))
