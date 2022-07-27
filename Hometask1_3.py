square_side = int(input("Введите длину стороны квадрата: "))
perimeter = square_side * 4
square = square_side * square_side
print(f'Вывод: \nПериметр: {perimeter} \nПлощадь:{square}')
rectangle_height = int(input("Введите высоту прямоугольника: "))
rectangle_width = int(input("Введите ширину прямоугольника: "))
perimeter = rectangle_height * 2 + rectangle_width * 2
square = rectangle_height * rectangle_width
print(f'Вывод: \nПериметр: {perimeter} \nПлощадь:{square}')
separator = input('Введите разделительный символ: ')
print(f' \n{separator * (perimeter + square)} \n')
salary = int(input('Введите заработную плату в месяц: '))
credit_percent = int(input('Введите, какой процент(%) уходит на ипотеку: '))
living_percent = int(input('Введите, какой процент(%) уходит на жизнь: '))
print(f'\nВывод: \nНа ипотеку было потрачено: {int(salary * credit_percent / 100 *12)} рублей \nБыло накоплено: {int((salary - (salary * credit_percent / 100) - (salary * living_percent / 100))*12)} рублей')