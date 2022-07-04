def div(*args):
    dividend = int(input("Введите делимое: "))
    divider = int(input("Введите делитель: "))

    if divider != 0:
        return dividend / divider
    else:
        print("Wrong number! Devider can't be null")

print(f'Результат:  {div()}')