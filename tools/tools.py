from core.state import STATE
import random

# def cart_add(item: str, cost: int):
#     STATE["cart"].append({
#         "name": item,
#         "price": cost
#     })
#     return f"Added {item} for ${cost}"

# def cart_total():
#     return sum(entry["price"] for entry in STATE["cart"])

# def cart_list():
#     return STATE["cart"]

def animal_get():
    rand_animal = random.choice(STATE["animals"])
    STATE["current_animal"] = rand_animal["name"]
    STATE["current_a_char"] = rand_animal["characteristics"]
    return rand_animal

def animal_char(user_guess: str):
    user_guess = user_guess.lower()
    characteristics = STATE["current_a_char"]
    for characteristic in characteristics:
        if user_guess == characteristic.lower():
            return True
        
def animal_name(user_guess: str):
    user_guess = user_guess.lower()
    current_animal = STATE["current_animal"].lower()

    if user_guess == current_animal:
        return "yes"
    else:
        return "no"