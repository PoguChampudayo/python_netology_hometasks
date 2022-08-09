class MoneyOperations:
    def __init__(self) -> None:
        self.salary = int(input('Введите заработную плату в месяц: '))
        self.credit_percent = int(input('Введите, какой процент(%) уходит на ипотеку: '))
        self.living_percent = int(input('Введите, какой процент(%) уходит на жизнь: '))
    def spend_money(self, salary, credit_percent):
        return salary * credit_percent // 100 *12
    def store_up_money(self, salary, credit_percent, living_percent):
        return (salary - (salary * credit_percent // 100) - (salary * living_percent // 100))*12
my_credit = MoneyOperations()
print(f'''
Вывод за год:
На ипотеку было потрачено: {my_credit.spend_money(my_credit.salary, my_credit.credit_percent)}
Было накоплено: {my_credit.store_up_money(my_credit.salary, my_credit.credit_percent, my_credit.living_percent)}''')