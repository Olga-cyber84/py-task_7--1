from pprint import pprint

file_name = 'recipes.txt'


def get_recipes(file_name):
    cook_book = {}
    dishes = {}
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            ingredients_quantity = file.readline()
            all_ingredients = []
            ingredients = {}
            for item in range(int(ingredients_quantity)):
                ingredient = file.readline()
                ingredient_name = ingredient.split('|')[0]
                quantity = ingredient.split('|')[1]
                measure = ingredient.split('|')[2]
                ingredients['ingredient_name'] = ingredient_name.strip()
                ingredients['quantity'] = int(quantity)
                ingredients['measure'] = measure.strip()
                all_ingredients.append(ingredients)
                ingredients = {}

            cook_book[dish_name] = all_ingredients
            file.readline()
    pprint(cook_book)
    return cook_book


get_recipes(file_name)
