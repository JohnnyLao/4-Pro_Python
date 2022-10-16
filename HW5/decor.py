import datetime


def logging(path):
    def new_logger(some_function):
        def new_function(*args, **kwargs):
            date = datetime.datetime.now().strftime('%x %X')
            result = f'Функция "new_logger" с аргументами {args} и {kwargs} вызвана {date}'
            with open(path, "w", encoding='utf-8') as f:
                f.write(result)
            return result
        return new_function
    return new_logger

