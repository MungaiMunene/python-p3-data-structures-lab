# data_structures.py

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
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # Return None if no match is found

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)  # Use floor division to get an integer result

def create_spicy_food(spicy_foods, new_food):
    spicy_foods.append(new_food)
    return spicy_foods

# Example usage (you can remove this before submission)
if __name__ == "__main__":
    print(get_names(spicy_foods))  # Example call
    print(get_spiciest_foods(spicy_foods))
    print_spicy_foods(spicy_foods)
    print(get_spicy_food_by_cuisine(spicy_foods, "American"))
    print_spiciest_foods(spicy_foods)
    print(average_heat_level(spicy_foods))
    new_food = {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
    print(create_spicy_food(spicy_foods, new_food))