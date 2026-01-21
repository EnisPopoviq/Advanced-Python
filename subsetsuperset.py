recipe_a = {'flour', 'sugar', 'eggs', 'milk', 'vanilla extract'}
recipe_b = {'flour', 'sugar', 'eggs'}

# recipe_b is a subset of recipe_a
# recipe_a is a superset of recipe_b

is_subset_result = recipe_b.issubset(recipe_a)
print("Is B subset of A?", is_subset_result)

is_subset_reverse = recipe_a.issubset(recipe_b)
print("Is A subset of B?", is_subset_reverse)

is_superset_result = recipe_a.issuperset(recipe_b)
print("Is A superset of B?", is_superset_result)