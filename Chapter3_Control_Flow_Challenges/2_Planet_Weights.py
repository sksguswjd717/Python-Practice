# 🧑‍🚀 Planet Weights

# HARD

# Instructions
# The year is 2199... we have become an interplanetary species and can travel to other planets in the solar system! 🚀

# Create a weight conversion program that:

# Asks the user what their Earth weight is (as a float).
# Asks the user for a planet number (as an int).
# Then, use an if/elif/else statement to calculate the user's weight on the destination planet.

# To calculate the user's weight:

# destination weight=Earth weight × relative gravity
# Number	Planet	Relative Gravity
# 1	Mercury	0.38
# 2	Venus	0.91
# 3	Mars	0.38
# 4	Jupiter	2.53
# 5	Saturn	1.07
# 6	Uranus	0.89
# 7	Neptune	1.14
# If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'.
your_weight = float(input('How much is your weight? '))
planet_number = int(input('What is your planet number? '))

if planet_number == 1:
  your_weight = your_weight * 0.38
  print('your weight is', your_weight)
elif planet_number == 2:
  your_weight = your_weight * 0.91
  print('your weight is', your_weight)
elif planet_number == 3:
  your_weight = your_weight * 0.38
  print('your weight is', your_weight)
elif planet_number == 4:
  your_weight = your_weight * 2.53
  print('your weight is', your_weight)
elif planet_number == 5:
  your_weight = your_weight * 1.07
  print('your weight is', your_weight)
elif planet_number == 6:
  your_weight = your_weight * 0.89
  print('your weight is', your_weight)
elif planet_number == 7:
  your_weight = your_weight * 1.14
  print('your weight is', your_weight)
else:
  print('Invalid planet number')
