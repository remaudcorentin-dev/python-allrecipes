# python-allrecipes
##### v0.1.2

Python API to search &amp; get recipes from the 'allrecipes.com' website (web crawler, unofficial)  
Useful, efficient and super simple to use.  

### Requirements :
`python >= 3.4`  
`beautifulsoup4 >= 4.6`  

### Usage :

```python

# Search :
query_options = {
  "wt": "pork curry"        # Query keywords
  "ingIncl": "olives"       # 'Must be included' ingrdients (optional)
  "ingExcl" "onions salad"  # 'Must not be included' ingredients (optional)
  "sort": "re"              # Sorting options : 're' for relevance, 'ra' for rating, 'p' for popular (optional)
}
query_result = AllRecipies.search(query_options)

# Get :
main_recipe_url = query_result[0]['url']
detailed_recipe = AllRecipes.get(main_recipe_url)

```

### API References

##### AllRecipes.search return a list of dictionary like :  
- name: name of the recipe.  
- description: short description of the recipe.  
- url: url of the detailed recipe on 'allrecipes.com'.  
- img: if exists, image of the recipe.  

##### AllRecipes.get return a dictionary like :  
- ingredients: string list of the recipe ingredients (including quantites)  
- steps: string list of each step of the recipe  

### OnGoing features :  
- Multiple returned images for the recipe  
- Preparation, Cooking time, Total Time, etc data  
- Multiple images returned for the search / get requests  
- Limit the number of returned query on search  


###### Support / Contact : remaudcorentin.dev@gmail.com
