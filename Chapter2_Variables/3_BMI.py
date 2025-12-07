"""
Docstring for Chapter2_Variables.08_BMI
08. BMI
# Modulo
Another operator that often trips people up is the modulo operator.

The % modulo operator doesn’t give you the result of a division – it gives you the remainder.

score = 5 % 3       # score is 2
score = 5 % 2       # score is now 1
score = 5 % 1       # score is now 0

5 divided by 3 is 1, with a remainder of 2.
5 divided by 2 is 2, with a remainder of 1.
5 divided by 1 is 5, with a remainder of 0.
We won’t use this right now, but we’ll come back to it later in the course.

# Exponents
Python can also perform exponentiation such as 2³ or 10².

In written math, we might see an exponent as a superscript number (like above), but typing superscripts isn't always easy on modern keyboards. Since exponentiation is super similar to multiplication, Python uses the notation **.

So 2 ** 3 is 2³ and 10 ** 2 is 10².

Here are more examples:

score = 2 ** 2      # score is 4
score = 2 ** 3      # score is now 8
score = 2 ** 4      # score is now 16

print(score)        # Output: 16

Let's give it a try!

Instructions
The body mass index (BMI) was created by a Belgian mathematician in the 1850s and it's used by health and nutrition professionals to quickly estimate body fat in certain populations.

The formula is pretty simple: Take an individual's weight (mass) in kilograms and dividing it by their height in meters, squared.


bmi= 
height 
2
 
mass
​
 

Create a bmi.py program that calculates your own BMI.

Author's note: Psst. BMI is an archaic and oversimplified way to measure personal health. It was created by a mathematician – not a doctor! 💡\
"""
bmi = 78 / 1.73**2
print(bmi)