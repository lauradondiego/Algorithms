#!/usr/bin/python
import math


def recipe_batches(recipe, ingredients):
    # recipe = amount needed
    # ingredients = amount available
    # result = amount available (ingr) // amount needed (recipe)
    # if any value in recipe > any in ingredients, return ZERO bc you can't make anything
    # if each value in recipe < each and every value in ingredients,
    # ^ perform integer division
    batches = math.inf
# ^ set possible batches to infinity to ensure you can never exceed the num of possible batches
# ^ we will rewrite this later with the actual num of batches we compute
    if len(recipe) > len(ingredients):
        return 0
        # this means that if what you need exceeds what you have, you can't
        # ^ make the recipe and you should just return 0. For 0 possible batches
    for i in recipe:
        if ingredients[i] < recipe[i]:
            return 0
            # ^ if the ingredients you have are less than the ingredients you need for the recipe
            # ^ return 0. This goes thru each index of the list, so every item one by one and repeats
        batch_calculation = ingredients[i] // recipe[i]
        # ^ set a new variable, using integer div // to check how many batches you can make with that specific item
        if batch_calculation < batches:  # less than infinity basically
            batches = batch_calculation
            # ^ then re write batches to equal this number of batches you can make

    return batches  # just return the number!


########## THOUGHT PROCESS BELOW ##############
    # if recipe['flour'] > ingredients['flour']:
    #   print("not enough ingredients available")
    # if recipe.values() > ingredients.values():
    #     print("not enough")
    #     print(recipe.values()[0])
    #     print(ingredients.values())
    # if recipe.values()[0] > ingredients.values()[0]:
    #     print("Not enough avail")
    #     print("Butter Need:", recipe.values()[0])
    #     print("Butter Have:", ingredients.values()[0])
    # print([ingredients.values()] // [recipe.values()])
    # print("you can make this", recipe.values())
    # if ingredients['butter'] > recipe['butter']:
    #     ingredients['butter'] // recipe['butter']
    # else:
    #     print("not enough ingredients")
    # print("RECIPE NEED:", recipe.items())
    # print("INGREDIENTS HAVE:", ingredients.items())
    # print(ingredients["milk"])
if __name__ == '__main__':
        # Change the entries of these dictionaries to test
        # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
