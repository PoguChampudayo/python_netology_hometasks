salary = int(input('Введите заработную плату в месяц: '))
credit_percent = int(input('Введите, какой процент(%) уходит на ипотеку: '))
living_percent = int(input('Введите, какой процент(%) уходит на жизнь: '))
print(f'\nВывод: \nНа ипотеку было потрачено: {int(salary * credit_percent / 100 *12)} рублей \nБыло накоплено: {int((salary - (salary * credit_percent / 100) - (salary * living_percent / 100))*12)} рублей')