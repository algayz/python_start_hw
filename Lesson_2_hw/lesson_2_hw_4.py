stroke = input("Введите строку из нескольких слов, разделённых пробелами: ")
word = []
num = 1

for e in range(stroke.count(' ') + 1):
    word = stroke.split()
    if len(str(word)) <= 10:
        print(f" {num} {word [e]}")
        num += 1
    else:
        print(f" {num} {word [e] [0:10]}")
        num += 1