def process_file(filename):
    f = open(filename, encoding="utf-8")
    text = f.read()
    text = text.replace(",", " ").replace("\n", " ").replace("-", " ")\
            .replace(".", " ").replace(":", " ").replace("–", " ").lower()
    return text

if __name__ == "__main__":
    text = process_file("data.txt")
    print(text)
