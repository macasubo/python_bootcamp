def usage():
	print("\nThis option does not exist, please type the corresponding number.\n"
			+ "To exit, enter 5.")

def add_recipe(name, ingredients, meal, prep_time):
	cookbook[name] = {
		"ingredients" : ingredients.split(" "),
		"meal" : meal,
		"prep_time" : prep_time}
	print("")

def delete_recipe(name):
	if name in cookbook:
		cookbook.pop(name)
		print("")
	else:
		print("\nNo recipe named " + name + "\n")

def print_recipe(name):
	if name in cookbook:
		print("\nRecipe for " + name + ":")
		print("Ingredients list: ", end='')
		print(cookbook.get(name).get("ingredients"))
		print("To be eaten for " + cookbook.get(name).get("meal") + ".")
		print("Takes " + cookbook.get(name).get("prep_time")
				+ " minutes of cooking.\n")
	else:
		print("\nNo recipe named " + name + "\n")

def print_cookbook():
	print("")
	for x in cookbook:
		print(x + " recipe :")
		for y in cookbook.get(x):
			print(y + ": ", end='')
			print(cookbook.get(x).get(y))
		print("")

cookbook = {
	"sandwich" : {
		"ingredients" : ["ham", "bread", "cheese", "tomatoes"],
		"meal" : "lunch",
		"prep_time" : "10"
	},
	"cake" : {
		"ingredients" : ["flour", "sugar", "eggs"],
		"meal" : "dessert",
		"prep_time" : "60"
	},
	"salad" : {
		"ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
		"meal" : "lunch",
		"prep_time" : "15"
	}
}

op = 0
while op != 5:
	option = input("Please select an option by typing the corresponding number:\n"
					+ "1: Add a recipe\n"
					+ "2: Delete a recipe\n"
					+ "3: Print a recipe\n"
					+ "4: Print the cookbook\n"
					+ "5: Quit\n>> ")
	if option.isdigit() == False:
		usage()
	else:
		op = int(option)
		if op < 1 or op > 6:
			usage()
		elif op == 1:
			add_recipe(
				input("\nEnter the recipe's name:\n>> "),
				input("Enter the recipe's ingredients, separated by spaces:\n>> "),
				input("Enter the recipe's type of meal:\n>> "),
				input("Enter the recipe's preparation time:\n>> "))
		elif op == 2:
			delete_recipe(input("\nPlease enter the recipe's name to delete\n>> "))
		elif op == 3:
			print_recipe(input("\nPlease enter the recipe's name to get its"
						+ " details:\n>> "))
		elif op == 4:
			print_cookbook()

print("\nCookbook closed.")
