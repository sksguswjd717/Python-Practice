"""
Docstring for Chapter3_Control_Flow.16_Sorting_Hat
The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

🦁 Gryffindor
🦅 Ravenclaw
🦡 Hufflepuff
🐍 Slytherin


Write a program that asks the user some questions with the int() and input() functions:

Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk

If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
Else, output the message "Wrong input."
Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold

If the answer is 1, Hufflepuff +2.
Else if answer is 2, Slytherin +2.
Else if answer is 3, Ravenclaw +2.
Else if answer is 4, Gryffindor +2.
Else, output the message "Wrong input."
Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum

If the answer is 1, Slytherin +4.
Else if the answer is 2, Hufflepuff +4.
Else if the answer is 3, Ravenclaw +4.
Else if the answer is 4, Gryffindor +4.
Else, output "Wrong input."
"""
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

q1 = int(input('Q1) Do you like Dawn or Dusk?\n    1) Dawn\n    2) Dusk\n'))

if q1 == 1:
  Gryffindor += 1
  Ravenclaw  += 1
elif q1 == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print('Wrong input')


q2 = int(input('Q2) When I’m dead, I want people to remember me as\n    1) The Good\n    2) The Great\n    3) The Wise\n    4) The Bold\n'))
if q2 == 1:
  Hufflepuff += 2
elif q2 == 2:
  Slytherin += 2
elif q2 == 3:
  Ravenclaw += 2
elif q2 == 4:
  Gryffindor += 2
else:
  print('Wrong input')

q3 = int(input('Q3) Which kind of instrument most pleases your ear?\n    1) The violin\n    2) The trumpet\n    3) The piano\n    4) The drum\n'))
if q3 == 1:
  Slytherin += 4
elif q3 == 2:
  Hufflepuff += 4
elif q3 == 3:
  Ravenclaw += 4
elif q3 == 4:
  Gryffindor += 4
else:
  print('Wrong input')

print('Slytherin : ', Slytherin)
print('Hufflepuff : ', Hufflepuff)
print('Ravenclaw : ', Ravenclaw)
print('Gryffindor : ', Gryffindor)