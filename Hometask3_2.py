persons = int(input('Введите число гостей: '))
# cook_book = [[
#                  'салат',
#                  [
#                      ['картофель', 100, 'гр.'],
#                      ['морковь', 50, 'гр.'],
#                      ['огурцы', 50, 'гр.'],
#                      ['горошек', 30, 'гр.'],
#                      ['майонез', 70, 'мл.'],
#                  ]
#              ],
#              [
#                  'пицца',
#                  [
#                      ['сыр', 50, 'гр.'],
#                      ['томаты', 50, 'гр.'],
#                      ['тесто', 100, 'гр.'],
#                      ['бекон', 30, 'гр.'],
#                      ['колбаса', 30, 'гр.'],
#                      ['грибы', 20, 'гр.'],
#                  ],
#              ],
#              [
#                  'фруктовый десерт',
#                  [
#                      ['хурма', 60, 'гр.'],
#                      ['киви', 60, 'гр.'],
#                      ['творог', 60, 'гр.'],
#                      ['сахар', 10, 'гр.'],
#                      ['мед', 50, 'мл.'],
#                  ]
#             ]]
# for i in cook_book:
#     print(f'\n{(i[0]).capitalize()}:')
#     for j in i[1]:
#         print(f'{j[0]}, {j[1] * persons}{j[2]}')

class Dish:
    def __init__(self) -> None:
        self.name = ''
        self.ingredients = []
        self.quantity = []
        self.unit = []
    def how_much_to_buy(self, quantity):
        print(f'{self.name}:')
        for i, ingredient in enumerate(self.ingredients):
            print(f'{ingredient}, {self.quantity[i] * persons}{self.unit[i]}')
        print()
salat = Dish()
salat.name = 'Салат'
salat.ingredients = ['картофель', 'морковь', 'огурцы', 'горошек', 'майонез']
salat.quantity = [100, 50, 50, 30, 70]
salat.unit = ['гр.', 'гр.', 'гр.', 'гр.', 'мл.']
pizza = Dish()
pizza.name = 'Пицца'
pizza.ingredients = ['сыр', 'томаты', 'тесто', 'бекон', 'колбаса', 'грибы']
pizza.quantity = [50, 50, 100, 30, 30, 20]
pizza.unit = ['гр.', 'гр.', 'гр.', 'гр.', 'гр.', 'гр.']
fruit_dessert = Dish()
fruit_dessert.name = 'Фруктовый десерт'
fruit_dessert.ingredients = ['хурма','киви','творог','сахар','мед']
fruit_dessert.quantity = [60, 60, 60, 10, 50]
fruit_dessert.unit = ['гр.', 'гр.', 'гр.', 'гр.', 'мл.']
salat.how_much_to_buy(persons)
pizza.how_much_to_buy(persons)
fruit_dessert.how_much_to_buy(persons)