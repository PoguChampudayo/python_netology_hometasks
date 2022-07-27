# Выведите на экран все уникальные гео-ID из значений словаря ids. Т.е. список вида [213, 15, 54, 119, 98, 35]
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
users = []
for user in list(ids.values()):
  users.extend(user)
print(sorted(list(set(users)), reverse = True))