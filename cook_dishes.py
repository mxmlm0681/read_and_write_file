import pprint

def my_cook_book():
    with open('recept.txt', encoding='utf-8') as file:
        cook_book = {}
        for txt in file.read().split('\n\n'):
            name, _ , *args = txt.split('\n')
            tmp = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                tmp.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = tmp
    return cook_book


pprint.pprint(my_cook_book(), width=100)

def get_shop_list_by_dishes(dishes, person_count):
    new_cook = {}
    for dish in dishes:
        if dish in my_cook_book():
            for ingredient in my_cook_book()[dish]:
                key, quantity, measure = ingredient.values()
                total_quantity = quantity * person_count
                if key in new_cook:
                    new_cook[key]["quantity"] += total_quantity
                else:
                    new_cook[key] = {"measure": measure,
                                     "quantity": total_quantity}
    return new_cook


pprint.pprint(get_shop_list_by_dishes(["Запеченный картофель", "Омлет", "Фахитос"], 2))


