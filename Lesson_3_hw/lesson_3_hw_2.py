def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])

print(my_func(name='Александр', surname='Петров', year='1987', city='Казань', email='alexpetrov87@mail.ru', telephone='+7(999)123-45-67'))