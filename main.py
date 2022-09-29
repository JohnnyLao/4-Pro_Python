from application import salary
from application.db1 import people
from datetime import datetime


if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    print(datetime.now())

