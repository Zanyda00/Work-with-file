with open('recipes.txt', 'r', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        quantity_ing = int(f.readline())
        composition = []
        for _ in range(quantity_ing):
            comp = f.readline().strip().split(' | ')
            ingredient_name, quantity, measure = comp
            composition.append({'ingredient_name': ingredient_name,
                                'quantity': int(quantity),
                                'measure': measure})
        f.readline()
        cook_book.update({dish_name: composition})


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for i in dishes:
        for ing in cook_book[i]:
            ingredient_name, quantity, measure = ing.values()
            if ingredient_name not in shop_list:
                shop_list.update({ingredient_name: {'measure': measure, 'quantity': quantity * person_count}})
            else:
                shop_list[ingredient_name]['quantity'] += quantity * person_count
    return shop_list


