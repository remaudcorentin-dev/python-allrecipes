from allrecipes import AllRecipes


# Fetch categories on main page
categories = AllRecipes.fetch_categories()

# Print all recipe categories available at the provided link
print(categories)

# Prints all recipe categories available on Allrecipes.com/recipes/96/salads-and-chili
# categories["Salad Recipes"] is the entire URL
print(AllRecipes.fetch_categories(categories["Salad Recipes"]))

# Search:
search_string = "pork curry"  # Query
query_result = AllRecipes.search(search_string)
print(query_result)

# Get:
main_recipe_url = query_result[0]['url']
# Get the details of the first returned recipe (most relevant in our case)
detailed_recipe = AllRecipes.get(main_recipe_url)

# Display result:
print("## %s:" % detailed_recipe['name'])  # Name of the recipe

print("### For %s servings:" % detailed_recipe['nb_servings'])
for ingredient in detailed_recipe['ingredients']:  # List of ingredients
    print("- %s" % ingredient)

for step in detailed_recipe['steps']:  # List of cooking steps
    print("# %s" % step)
