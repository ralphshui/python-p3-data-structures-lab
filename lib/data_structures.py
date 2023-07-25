spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        spiciest_foods = []
        if food["heat_level"] > 5:
            spiciest_foods.append(food)
        return spiciest_foods
    
    # spiciest_foods = []
    # i=0
    # while i < len(spicy_foods): 
    #     if spicy_foods[i]["heat_level"] > 5:
    #         spiciest_foods.append(spicy_foods[i])
    #     i+=1
    # return spiciest_foods
   
    # spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    # return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    
    # cuisine_foods = [food for food in spicy_foods if food["cuisine"] == cuisine]
    # return cuisine_foods THIS DOES NOT PASS FOR SOME REASON??


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_average_heat_level(spicy_foods):
    all_heat =[]
    for food in spicy_foods:
        all_heat.append(food['heat_level'])
    
    return (sum(all_heat)/len(all_heat))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
