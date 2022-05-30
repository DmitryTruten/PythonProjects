filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"{filename} doesn't exists")

else:
    # Count all words in file
    words = contents.split()
    num_words = len(words)
    print(f"{filename} has about {num_words} words.")