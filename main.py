from prettytable import PrettyTable
from datetime import datetime
from dateutil.relativedelta import relativedelta


def ann_in(summ_credit, perc_credit, period_credit):  # Функция принимает сумму кредита, процентную ставку и срок
    r = perc_credit / 1200
    K = (r * (1 + r) ** period_credit) / (((1 + r) ** period_credit) - 1)
    summ_month = summ_credit * K  # Месячный платеж
    total = summ_month * period_credit  # Общий долг с процентами
    today = datetime.today()  # Дата сегодня
    payments = []  # Создаю список для списков платежей

    for month_i in range(1, period_credit + 1):  # Идет перебор по количеству месяцев указанных как срок кредита
        curr_month_date = today + relativedelta(months=month_i)  # Каждый раз добавляет месяц от текущей даты
        curr_month_str = curr_month_date.strftime('%b')  # Замена числа на конкретный месяц (слово)
        (total - summ_credit) / (total - summ_month * (month_i - 1)) * (total - summ_month * (month_i - 1))
        curr_payment = [
            curr_month_str,
            summ_month,
            total - summ_month * (month_i - 1),
            total - summ_credit,
            total - summ_month * month_i
        ]  # Список платежа по месяцам. С пошаговым уменьшением текущего долга
        payments.append(curr_payment)  # Запись списков в список платежей

    return payments


summ_credit = int(input('Введите сумму кредита: '))
perc_credit = float(input('Введите процентную ставку: '))
period_credit = int(input('На сколько месяцев взят кредит: '))

payments = ann_in(summ_credit, perc_credit, period_credit)  # Вызов функции
mytable = PrettyTable()  # Создание таблицы
mytable.field_names = ['Месяц', 'Ежемесячный платеж', 'Основной долг', 'Долг по процентам', 'Остаток основного долга']

for el in payments:
    mytable.add_row(el)  # Заполнение строк нашими списками платежей по месяцам
print(mytable)  # вывод таблицы в терминал
