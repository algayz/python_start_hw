my_list = [7, 5, 3, 3, 2]

print(f"Рейтинг - {my_list}")

num = int(input("Введите число: "))

i = 0

for n in my_list:
    if num <= n:
        i += 1
    elif num > n:
        break

my_list.insert(i, float(num))
print(my_list)