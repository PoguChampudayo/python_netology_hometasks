# Напишите код для преобразования произвольного списка вида ['2018-01-01', 'yandex', 'cpc', 100] (он может быть любой длины) в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}
my_list = [1, 2, 3, 4, 5, 6, 7]
result = {my_list[-2]: my_list[-1]}
for element in my_list[:-2][::-1]:
  result = {element:result}
print(result)
