#! /usr/bin/env python
"""reducer.py"""

import sys


def perform_reduce():
    date = None  # дата (год - месяц)
    current_date = None  # текущая дата (год - месяц)

    payment_type = None  # вид отплаты
    current_payment_type = None  # текущий вид оплаты

    # переменные ниже нужны для подсчета среднего Tips average amount

    current_count_trips = 0  # текущее число поездок
    current_sum_tip_amount = 0  # текущая сумма tip_amount

    for line in sys.stdin:
        line = line.strip()
        date, payment_type, tip_amount = line.split('\t')

        # год = 2020, месяц от 1 до 12, payment_type от 1 до 8, tip_amount положительный
        try:
            int(date[:4]) == 2020 and int(date[5:7]) in range(1, 13) and int(payment_type) in range(1, 9) and float(
                tip_amount) > 0
        except:
            continue

        # если все данные корректные, то группируем
        # первое вложение - группировка по месяцам
        # второе вложение - группировка по payment_type

        # если текущая дата = дате и текущий метод оплаты = методу оплаты, увеличиваю количество поездок на 1 и tip_payment на величину tip_payment
        if current_date == date:
            if current_payment_type == payment_type:
                current_count_trips += 1
                current_sum_tip_amount += int(tip_amount)
        else:
            if current_date:
                print('%s\t%s\t%s' % (current_date, current_payment_type, tip_amount))
            current_date = date
            current_payment_type = payment_type
            current_sum_tip_amount = tip_amount

        if current_date == date:
            if current_payment_type == payment_type:
                print('%s\t%s\t%s' % (current_date, current_payment_type, tip_amount))


if __name__ == '__main__':
    perform_reduce()
