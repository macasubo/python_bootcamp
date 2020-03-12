from book import Book
from recipe import Recipe

myrecipe = Recipe("LaRecette", 2, 42, ["a", "b", "c"],
					"this is the decription", "lunch")

print(str(myrecipe))

mybook = Book("LeLivre", None, None, {"sarter": [],
				"lunch": [myrecipe, myrecipe], "dessert": []})
print("")
mybook.get_recipe_by_name("LaRecette")
print("")
for recipe_name in mybook.get_recipes_by_types("lunch"):
	print(recipe_name)
print("")
new_recipe = myrecipe
new_recipe.name = ("new_recipe")
mybook.add_recipe(new_recipe)
mybook.get_recipe_by_name("new_recipe")
