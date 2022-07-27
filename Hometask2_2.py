month = input('Введите месяц: ').capitalize()
date_number = int(input('Введите число: '))
print(month,date_number)
if (month == 'Декабрь' and 22 <= date_number <= 31) or (month == 'Январь' and 1 <= date_number <= 20):
    zodiac = 'Козерог'
elif (month == 'Январь' and 21 <= date_number <= 31) or (month == 'Февраль' and 1 <= date_number <= 19):
    zodiac = 'Водолей'
elif (month == 'Февраль' and 20 <= date_number <= 29) or (month == 'Март' and 1 <= date_number <= 20):
    zodiac = 'Рыбы'
elif (month == 'Март' and 21 <= date_number <= 31) or (month == 'Апрель' and 1 <= date_number <= 20):
    zodiac = 'Овен'
elif (month == 'Апрель' and 21 <= date_number <= 30) or (month == 'Май' and 1 <= date_number <= 21):
    zodiac = 'Телец'
elif (month == 'Май' and 22 <= date_number <= 31) or (month == 'Июнь' and 1 <= date_number <= 21):
    zodiac = 'Близнецы'
elif (month == 'Июнь' and 22 <= date_number <= 30) or (month == 'Июль' and 1 <= date_number <= 22):
    zodiac = 'Рак'
elif (month == 'Июль' and 23 <= date_number <= 31) or (month == 'Август' and 1 <= date_number <= 21):
    zodiac = 'Лев'
elif (month == 'Август' and 22 <= date_number <= 31) or (month == 'Сентябрь' and 1 <= date_number <= 23):
    zodiac = 'Дева'
elif (month == 'Сентябрь' and 24 <= date_number <= 30) or (month == 'Октябрь' and 1 <= date_number <= 23):
    zodiac = 'Весы'
elif (month == 'Октябрь' and 24 <= date_number <= 31) or (month == 'Ноябрь' and 1 <= date_number <= 22):
    zodiac = 'Скорпион'
elif (month == 'Ноябрь' and 23 <= date_number <= 30) or (month == 'Декабрь' and 1 <= date_number <= 21):
    zodiac = 'Стрелец'
else:
  print('Введена некорректная дата')
print('Вывод:\n' , zodiac)