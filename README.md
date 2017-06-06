# python-allrecipes
Python API to search &amp; get recipes from the 'allrecipes.com' website (web crawler)
Useful, efficient and super simple to use.

Usage :

```python

# Search :
query_options = {
  "wt": "pork curry"        # Query keywords
  "ingIncl": "olives"       # 'Must be included' ingrdients (optional)
  "ingExcl" "onions salad"  # 'Must not be included' ingredients (optional)
  "sort": "re"              # Sorting options : 're' for relevance, 'ra' for rating, 'p for popular (optional)
}
query_result = AllRecipies.search(query_options)

# Get :
main_recipe_url = query_result[0]['url']
detailed_recipe = AllRecipes.get(main_recipe_url)

```
