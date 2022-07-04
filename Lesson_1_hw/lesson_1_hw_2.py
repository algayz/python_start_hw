sec = int(input('Введите время в секундах: '))

sec_value = sec % (24 * 3600)
hour_value = sec_value // 3600
sec_value %= 3600
min_value = sec_value // 60
sec_value %= 60

print("%02d:%02d:%02d" % (hour_value, min_value, sec_value))