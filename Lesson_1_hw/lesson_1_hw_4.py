number = int(input('Введите целое положительное число: '))
max = number % 10
num = number

while num > 0:
    n = num % 10
    if n > max:
        max = n

    if n == 9:
        break

    num //= 10

print(f"Наибольшая цифра в числе {number} равна {max}")