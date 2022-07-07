def salary():
    try:
        time = float(input('Кол-во рабочиз часов: '))
        salary = int(input('Ставка в час в RUB: '))
        bonus = int(input('Премия (RUB): '))
        total = time * salary + bonus
        print(f'Доходы сотрудника составят: {total}')
    except ValueError:
        return print('Not a number')

salary()