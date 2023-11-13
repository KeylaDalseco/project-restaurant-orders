import csv
from typing import Set, Dict
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes: Set[Dish] = set()
        self._read_menu_data()

    def _read_menu_data(self) -> None:
        with open(self.source_path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            menu_data = list(csv_reader)

        dishes_dict: Dict[str, Dish] = {}

        for row in menu_data:
            dish_name, dish_price, ingredient_name, quantity = row

            dish = dishes_dict.get(dish_name)
            if not dish:
                dish_price = float(dish_price.replace('R$', '')
                                   .replace(',', '.'))
                dish = Dish(name=dish_name, price=dish_price)
                dishes_dict[dish_name] = dish
                self.dishes.add(dish)

            ingredient = Ingredient(name=ingredient_name)
            dish.add_ingredient_dependency(ingredient, int(quantity))
