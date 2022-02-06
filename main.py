from prettytable import PrettyTable
from datetime import datetime
from dateutil.relativedelta import relativedelta


def ann_in(summ_credit, perc_credit, period_credit):
    r = perc_credit / 1200
    K = (r * (1 + r) ** period_credit) / (((1 + r) ** period_credit) - 1)
    summ_month = summ_credit * K
    total = summ_month * period_credit

    today = datetime.today()
    payments = []

    for month_i in range(1, period_credit + 1):
        curr_month_date = today + relativedelta(months=month_i)
        curr_month_str = curr_month_date.strftime('%b')
        curr_payment = [
            curr_month_str,
            summ_month,
            total,
            total - summ_credit,
            total - summ_month * month_i
        ]
        payments.append(curr_payment)

    return payments


summ_credit = int(input('Введите сумму кредита: '))
perc_credit = float(input('Введите процентную ставку: '))
period_credit = int(input('На сколько месяцев взят кредит: '))

payments = ann_in(summ_credit, perc_credit, period_credit)

mytable = PrettyTable()
# имена полей таблицы
mytable.field_names = ['Месяц', 'Ежемесячный платеж', 'Основной долг', 'Долг по процентам', 'Остаток основного долга']
# добавление данных по одной строке за раз
for el in payments:
    mytable.add_row(el)
# вывод таблицы в терминал
print(mytable)

