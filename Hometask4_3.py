# Дан список поисковых запросов. Получить распределение количества слов в них. Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'надо больше слов в запросе',
    'чтобы проверить правильность программы',
    'вотъ',
    'а еще надо пустой запрос сделать',
    ''
    ]
queries_length = {}
j = 0
max_length = max([len(query.split()) for query in queries])
for i in range(max_length + 1):
  queries_length[i] = 0
for query in queries:
  queries_length[len(query.split())] += 1
for percentage in list(queries_length.values()):
  print(f'Запросов, состоящих из {j} слов - {round(percentage * 100 / len(queries), 2)}%')
  j += 1