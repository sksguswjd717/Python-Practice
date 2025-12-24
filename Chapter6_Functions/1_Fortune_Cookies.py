# import random

# def fortune():
#     random_number = random.randint(1,8)
#     if random_number == 1:
#         print("Don't pursue happiness – create it.")
#     elif random_number == 2:
#         print("All things are difficult before they are easy.")
#     elif random_number == 3:
#         print("The early bird gets the worm, but the second mouse gets the cheese.")
#     elif random_number == 4:
#         print("Someone in your life needs a letter from you.")
#     elif random_number == 5:
#         print("Don't just think. Act!")
#     elif random_number == 6:
#         print("Your heart will skip a beat.")
#     elif random_number == 7:
#         print("The fortune you search for is in another cookie.")
#     else:
#         print("Help! I'm being held prisoner in a Chinese bakery!")

# fortune()

# This is bad code ↑↑↑↑

import random

# data should be in data structure!!

options = [
    "Don't pursue happiness – create it.",
    "All things are difficult before they are easy.",
    "The early bird gets the worm, but the second mouse gets the cheese.",
    "Someone in your life needs a letter from you.",
    "Don't just think. Act!",
    "Your heart will skip a beat.",
    "The fortune you search for is in another cookie.",
    "Help! I'm being held prisoner in a Chinese bakery!",
    ]

def fortune():
    rand_number = random.randint(0,7)
    print(options[rand_number])

fortune()
fortune()
fortune()