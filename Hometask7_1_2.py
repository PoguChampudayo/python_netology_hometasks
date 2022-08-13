from encodings import utf_8

class Recipe_file:

    def __init__(self) -> None:
        self.dish_name = ''
        self.ingredients_quantity = 0
        self.ingredients = []
        
    def get_all_recipes(self, filepath):
        result = {}
        with open(filepath, 'r', encoding='utf-8') as file:
            sample = file.readlines()
            for element in sample:
                if element.strip('\n') == '':
                    result[self.dish_name] = self.ingredients
                    self.ingredients = []
                elif '|' in element.strip('\n'):
                    self.ingredients.append({'ingredient_name': element.strip('\n').split(' | ')[0], 
                                             'quantity': element.strip('\n').split(' | ')[1], 
                                             'measure': element.strip('\n').split(' | ')[2]})
                elif element.strip('\n').isdigit():
                    self.ingredients_quantity = int(element.strip('\n'))
                else:
                    self.dish_name = element.strip('\n')
            result[self.dish_name] = self.ingredients
        return result

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in result:
                result[ingredient['ingredient_name']] = ({'measure': ingredient['measure'], 
                                                      'quantity': int(ingredient['quantity']) * person_count})
            else:
                result[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
    return result
cook_book_recipes = Recipe_file()
cook_book = cook_book_recipes.get_all_recipes('support_files/recipes.txt')
print(get_shop_list_by_dishes(['Омлет','Фахитос'],3))
