"""
07. Temperature
# Operators
Computers are incredible at doing math calculations. Now that we have learned about variables, let's use them with arithmetic operators to calculate things! 🔢

Python has the following arithmetic operators:

+ Addition
- Subtraction
* Multiplication
/ Division
score = 0           # score is 0
score = 4 + 3       # score is now 7
score = 4 - 3       # score is now 1
score = 4 * 3       # score is now 12
score = 4 / 3       # score is now 1.3333

print(score)        # Output: 1.3333

And take a look at this code that calculates a 20% tip by calculating the total and then multiplying by a float (decimal number):

pizza = 2.99
coke = 0.99

total = pizza + coke

tip = total * 0.2

print(tip) # Output: 0.796

Another way to write this is using parentheses to calculate the total and the tip in one line:

tip = (pizza + coke) * 0.2

In Python, parentheses have the highest order of operations, just like PEMDAS.

Now that we've learned about the basics of variables and operators, let's put them to use!

Instructions
Create a temperature.py program that converts a number from Fahrenheit (°F) to Celsius (°C).

Google the current temperature of Brooklyn, NY (where Codédex is based) in °F.

Use the following formula and write it out in Python:


Celsius= 
1.8
(Fahrenheit−32)
​
 

Print out the converted temperature. 🌡️
"""

# Write code below 💖

#7 = (x - 32) / 1.8
c = (44.6 - 32) / 1.8
print(c)