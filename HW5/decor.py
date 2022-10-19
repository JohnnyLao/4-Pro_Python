import datetime


def decor(old_function):
    def new_function(*args, **kwargs):
        date = datetime.datetime.now().strftime('%x %X')
        result = f'Функция {old_function} с аргументами {args} и {kwargs} вызвана {date} decor'
        with open("log.txt", "w", encoding='utf-8') as f:
            f.write(result)
        return result
    return new_function


def parametrized_decor(parameter):
    def decor(old_function):
        def new_function(*args, **kwargs):
            date = datetime.datetime.now().strftime('%x %X')
            result = f'Функция {old_function} с аргументами \n{args} и {kwargs} \nвызвана {date} parametrized_decor'
            with open(parameter, "w", encoding='utf-8') as f:
                f.write(result)
            return result
        return new_function
    return decor




