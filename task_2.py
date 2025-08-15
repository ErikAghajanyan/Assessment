'''Задача 2. Работа с текущим временем и датой
Напишите скрипт, который получает текущее время и дату, а затем выводит их в
формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
недели в году.'''

from _datetime import datetime

def date_formater():
    present_time = datetime.now()
    formatter_time = present_time.strftime('%Y-%m-%d %H:%M:%S')
    day_of_week = present_time.strftime('%A')
    week_number = present_time.isocalendar()[1]
    print(f'Current date and time {formatter_time}')
    print(f'Day of the week: {day_of_week}')
    print(f'Week number: {week_number}')

if __name__ == '__main__':
    date_formater()
