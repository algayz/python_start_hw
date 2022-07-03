count = int(input("Введите количество элементов списка "))
data = []

i = 0
c = 0

while i < count:
    data.append(input("Введите следующее значение списка "))
    i += 1

for element in range(int(len(data)/2)):
    data[c], data[c + 1] = data[c + 1], data[c]
    c += 2

print(data)