from tools.tools import *

TOOLS = {
    # "cart_add": cart_add,
    # "cart_total": cart_total,
    # "cart_list": cart_list,

    "animal_get": animal_get,
    "animal_char": animal_char,
    "animal_name": animal_name,
}

TOOL_DESCRIPTIONS = {
    # "cart_add": "Add an item to the cart. args: item:str, cost:int",
    # "cart_total": "Return total cost of all items in cart. args: none",
    # "cart_list": "Return all items currently in cart. args: none",

    "animal_get": "Gets a random animal for guessing. args: none",
    "animal_char": "Returns only the word yes or no for if the randomly selected animal has that characteristic. args: user_guess: str",
    "animal_name": "Returns true or false by checking if the randomly selected animal has the same name. args: user_guess: str"
}