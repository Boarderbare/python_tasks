with open("file_reciepes.txt", encoding='utf8') as f:
    reciepes = {}
    while True:
   
        dish = f.readline().strip()
        if not dish:
            break
        amount_ingredients = int(f.readline().strip())
        list_ingredients = []
        for item in range(amount_ingredients):
            list_of_values = [value.strip() for value in f.readline().split('|')]
            one_ingredient = dict(
                zip(('ingredient_name', 'quantity', 'measure'),
                    (list_of_values)))
            list_ingredients.append(one_ingredient)
        f.readline()
        reciepes[dish] = list_ingredients
        print(dish)
        print(amount_ingredients)
        print(list_ingredients, end='\n\n')

def get_shop_list_by_dishes(dishes, person):
        total_ing= {}
        for item in dishes:
            if item in reciepes:
                print(f'\n{item.capitalize()}:')
                for ing in reciepes[item]:
                    if ing["ingredient_name"] in total_ing:
                        new_amount=int(ing["quantity"])
                        prev_amount= int(total_ing[ing["ingredient_name"]][0])
                        total_ing[ing["ingredient_name"]]= [prev_amount+new_amount,ing["measure"]]
                    else:    
                        total_ing[ing["ingredient_name"]]= [int(ing["quantity"]),ing["measure"]]
                    print(ing["ingredient_name"] +" - "+ (str(person*int(ing["quantity"])))+str(ing["measure"]))
        
        print(f"\n Total ingridients: {total_ing}")
get_shop_list_by_dishes(["Фахитос", "Омлет"], 2)
