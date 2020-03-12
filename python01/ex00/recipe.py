import sys

class Recipe:
	def __init__(recipe, name, cooking_lvl, cooking_time,
				ingredients, description, recipe_type):
		try:
			recipe.name = str(name)
			recipe.cooking_lvl = int(cooking_lvl)
			if recipe.cooking_lvl < 1 or recipe.cooking_lvl > 5:
				print("ERROR\ncooking_lvl out of range")
				sys.exit()
			recipe.cooking_time = int(cooking_time)
			if recipe.cooking_time < 0:
				print("ERROR\ncooking_time cannot be negative")
				sys.exit()
			recipe.ingredients = ingredients
			recipe.description = str(description)
			recipe.recipe_type = str(recipe_type)
			if recipe.recipe_type not in ["starter", "lunch", "dessert"]:
				print("ERROR\ninvalid recipe type")
		except ValueError as e:
			print(f'ValueError : {e}')
			sys.exit()

	def __str__(self):
		return '\n'.join([f'{key}: {value}' for key, value in self.__dict__.items()])
