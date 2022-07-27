
boys = list(input('Введите имена парней (разделяя пробелами): ').split())
girls = list(input('Введите имена девушек (разделяя пробелами): ').split())
boys.sort()
girls.sort()
result = zip(boys, girls)
print('Идеальные пары: ')
for couple in result:
  print(f'{couple[0]} и {couple[1]}')
if len(boys) != len(girls):
  print('Кто-то может остаться без пары!')