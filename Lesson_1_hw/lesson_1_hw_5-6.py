revenue = int(input('Введите вашу выручку: '))
cost = int(input('Введите ваши издержки: '))

if revenue < cost:
    print('Ваша организация работает в убыток.')

elif revenue == cost:
    print('Ваша организация работает в ноль.')

elif revenue > cost:
    print('Ваша организация приносит прибыль.')
    profit = revenue - cost
    print('Прибыль вашей компании составляет: ' + str(profit) + '₽')
    workforce = int(input('Сколько сотрудников у вас работает? '))
    profit_2 = profit / workforce
    print('Каждый сотрудник приносит вам: ' + str(profit_2) + '₽')