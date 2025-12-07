"""
Docstring for 14_magic8
# Random
In Python, modules are .py files containing Python code that can be imported inside another Python program. The Python standard library contains well over 200 modules that we can use.

We can use the .randint() function from a module called random to generate a random number from a range.

But first, let's import this module so we can use its functions.

import random

Next, we'll create a variable to store the randomly generated value. Declare a variable called num, and assign it to the function call:

num = random.randint(1, 9)

This will generate a random number between 1 and 9 (inclusive of both).

Together, the code will look like:

import random

num = random.randint(1, 9)

print(num)

Try running this code! ☝️

The output should be different each time it runs: 2, 8, 5, 9, 2, 1, 3...

Instructions
The Magic 8 Ball is a popular office toy and children's toy invented in the 1940s for fortune-telling and advice seeking. 🎱

It's an oversized 8 ball with some of the following answers:

Yes - definitely.
It is decidedly so.
Without a doubt.
Reply hazy, try again.
Ask again later.
Better not tell you now.
My sources say no.
Outlook not so good.
Very doubtful.
Create a magic8.py program that can respond to any Yes or No questions with a different answer each time it executes.

The output should have the following format:

Question:      [Question]
Magic 8 Ball:  [Answer]

For example:

Question:      Is Codédex better than Udemy yet?
Magic 8 Ball:  Better not tell you now.
"""
import random

num = random.randint(1, 9)

input('Question:    ')

if num == 1:
  print('Magic 8 Ball:    Yes - definitely.')
elif num == 2:
  print('Magic 8 Ball:    It is decidedly so.')
elif num == 3:
  print('Magic 8 Ball:    Without a doubt.')
elif num == 4:
  print('Magic 8 Ball:    Reply hazy, try again.')
elif num == 5:
  print('Magic 8 Ball:    Ask again later.')
elif num == 6:
  print('Magic 8 Ball:    Better not tell you now.')
elif num == 7:
  print('Magic 8 Ball:    My sources say no.')
elif num == 8:
  print('Magic 8 Ball:    Outlook not so good.')
else:
  print('Magic 8 Ball:    Very doubtful.')
