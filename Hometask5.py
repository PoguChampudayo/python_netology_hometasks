documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
             ]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
              }

def find_name(documents):
  doc_number = input('Введите номер документа: ')
  for document in documents:
    if doc_number == document['number']:
      print(f'Имя владельца документа: {document["name"]}')
      return
  print('Имя владельца не найдено')
  
def find_shelf(directories):
  doc_number = input('Введите номер документа: ')
  for shelf in directories.items():
    if doc_number in shelf[1]:
      print(f'Номер полки: {shelf[0]}')
      return
  print('Такого документа нет на полках')
  
def show_all_docs(documents):
  for document in documents:
    print(f'{document["type"]} \"{document["number"]}\" \"{document["name"]}\"')
    
def add_doc(documents, directories):
  doc_type = input('Введите тип документа: ')
  doc_number = input('Введите номер документа: ')
  doc_name = input('Введите имя владельца: ')
  shelf_number = input('Введите номер полки: ')
  if shelf_number not in list(directories.keys()):
    print('Ошибка: неверно выбрана полка')
  else:
    documents.append({"type": doc_type, "number": doc_number, "name": doc_name})
    directories[shelf_number].append(doc_number)
  
    
def delete_doc(documents):
  doc_number = input('Введите номер документа: ')
  for document in documents:
    if doc_number == document["number"]:
      documents.remove(document)
  for shelf in directories:
    if doc_number in directories[shelf]:
      directories[shelf].remove(doc_number)
      return
  print('Документа не существует')
  
def move_doc(directories):
  doc_number = input('Введите номер документа: ')
  shelf_number = input('Введите номер полки, на которую хотите переместить документ: ')
  if shelf_number not in list(directories.keys()):
    print('Ошибка: неверно выбрана полка')
    return
  for shelf in directories.items():
    if doc_number in shelf[1]:
      directories[shelf_number].append(directories[shelf[0]].pop(directories[shelf[0]].index(doc_number)))
      return
  print('Ошибка: документ не найден')
  
def add_shelf(directories):
  shelf_number = input('Введите номер полки, которую хотите добавить: ')
  if shelf_number not in list(directories.keys()):
    directories[shelf_number] = []
  else:
    print('Полка с таким номером уже существует')
    
def help_me():
  print('p - Вывод имени владельца документа\ns - Вывод номера полки, где лежит документ\nl - Вывод всех документов\na - Добавление нового документа\nd - Удаление документа\nm - Перемещение документа с одной полки на другую\nas - Добавление новой полки\nq - Выход из программы')
  
def main():
  while True:
    command = input('Введите команду (h - вывод списка команд): ')
    if command == 'h':
      help_me()
    elif command == 'p':
      find_name(documents)
    elif command == 's':
      find_shelf(directories)
    elif command == 'l':
      show_all_docs(documents)
    elif command == 'a':
      add_doc(documents, directories)
    elif command == 'd':
      delete_doc(documents)
    elif command == 'm':
      move_doc(directories)
    elif command == 'as':
      add_shelf(directories)
    elif command == 'q':
      return
    else:
      print('Команда введена неверно')
main()