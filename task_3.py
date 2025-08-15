'''Задача 3. Планирование задач
Напишите функцию, которая принимает количество дней от текущей даты и
возвращает дату, которая наступит через указанное количество дней. Дополнительно,
выведите эту дату в формате YYYY-MM-DD.
'''
from datetime import datetime, timedelta

def get_new_date(days):
    cur_date = datetime.now()
    future_date = cur_date + timedelta(days=days)
    date_formatter = future_date.strftime('%Y-%m-%d')
    return date_formatter

if __name__ == '__main__':
    print(get_new_date(10))
