# python-allrecipes
##### v0.3.1


###### News : package now up to date on 2023-02-20 to include recent 'allrecipies.com' website html changes + fix SSL issue

Python API to search &amp; get recipes from the 'allrecipes.com' website (web crawler, unofficial)  
Useful, efficient and super simple to use.  

### Installation :
`pip install python-allrecipes==0.3.1`  


### Requirements :
`python >= 3.4`  
`beautifulsoup4 >= 4.6`  

### API References

##### AllRecipes.search return a list of dictionary like :  
- name: name of the recipe.  
- url: url of the detailed recipe on 'allrecipes.com'.  
- image: if exists, image of the recipe.  
- rating: average rating given to the recipe (float 0 - 5, `None` if does not exist)

##### AllRecipes.get return a dictionary like :  
- rating: average rating given to the recipe (float 0 - 5, `None` if does not exist)
- ingredients: string list of the recipe ingredients (including quantities)  
- steps: string list of each step of the recipe  
- prep_time: Estimated preparation time of the recipe (>= 0.1.6)
- cook_time: Cooking time (>= 0.1.6)
- total_time: Estimated total time of the recipe (>= 0.1.6)
- nb_servings: Estimated number of servings for the recipe (>= 0.3.1)

### Usage / Example:

```python
from allrecipes import AllRecipes

# Search:
search_string = "pork curry"  # Query
query_result = AllRecipes.search(search_string)

# Get:
main_recipe_url = query_result[0]['url']
detailed_recipe = AllRecipes.get(main_recipe_url)  # Get the details of the first returned recipe (most relevant in our case)

# Display result:
print("## %s:" % detailed_recipe['name'])  # Name of the recipe

print("### For %s servings:" % detailed_recipe['nb_servings'])
for ingredient in detailed_recipe['ingredients']:  # List of ingredients
    print("- %s" % ingredient)

for step in detailed_recipe['steps']:  # List of cooking steps
    print("# %s" % step)

```


### Notes:
Since version 0.3:
- Search only supports text as other options are not avilable on allrecipes website anymore,
- 'description' from the search result is not available anymore as it is not returned on search by allrecipes anymore

### OnGoing features :  
- ~~Preparation time, Cooking time, Total time~~ (available in 0.1.6)  
- Calories counter / Nutritionals apports
- Multiple images returned for the search / get requests  
- Limit the number of returned query on search  
- More returned data & query options

Related projects :  
- https://github.com/remaudcorentin-dev/python-marmiton

###### Support / Contact : remaudcorentin.dev@gmail.com
