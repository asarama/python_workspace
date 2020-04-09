from random import randint
import singleton

def add_random_items(number_of_items = randint(1, 10)):
    while number_of_items > 0:
        singleton.add_to_list(randint(-99,99))
        number_of_items -= 1