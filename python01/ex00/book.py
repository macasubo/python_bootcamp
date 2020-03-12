import sys
import datetime
from recipe import Recipe

class Book:
	def __init__(self, name, last_update, creation_date, recipes_list):
		self.name = str(name)
		self.last_update = datetime.datetime.now()
		self.creation_date = datetime.datetime.now()
		self.recipes_list = recipes_list

	def get_recipe_by_name(self, name):
		for key, values in self.__dict__["recipes_list"].items():
			for recipe in values:
				if recipe.name == name:
					print(str(recipe))
					return(recipe)
	
	def get_recipes_by_types(self, recipe_type):
		name = list(())
		for recipe in self.__dict__["recipes_list"][recipe_type]:
			name.append(recipe.name)
		return name

	def add_recipe(self, recipe):
		if not isinstance(recipe, Recipe):
			print("ERROR: incorrect recipe format\n")
		else:
			self.last_update = datetime.datetime.now()
			for i in self.__dict__["recipes_list"]:
				if i == recipe.recipe_type:
					self.__dict__["recipes_list"][i].append(recipe)
