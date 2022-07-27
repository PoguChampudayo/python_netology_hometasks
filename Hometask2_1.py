credit_rate = 6
region = input('Введите ваш регион: ')
children_quantity = int(input('Введите количество детей: '))
salary_program = input('У вас есть зарплатный проект в этом банке? (да/нет) ')
if salary_program.lower() == 'да':
    salary_program = True
else:
    salary_program = False
insurance = input('Вы будете оформлять страховку в нашем банке? (да/нет) ')
if insurance.lower() == 'да':
    insurance = True
else:
    insurance = False
if region.lower(
) == 'амурская область' or 'республика бурятия' or 'евренйская автономная область' or 'забайкальский край' or 'камчатский край' or 'магаданская область' or 'приморский край' or 'республика саха (якутия)' or 'сахалинская область' or 'хабаровский край' or 'чукотский автономный округ' or 'дальный восток':
    credit_rate = 2.0
else:
    if children_quantity > 3:
        credit_rate -= 0.5
    if salary_program:
        credit_rate -= 0.5
    if insurance:
        credit_rate -= 1.5
if credit_rate % 1 == 0:
    credit_rate = int(credit_rate)
print(f'\nВаша кредитная ставка: {credit_rate}%')
