"""
Docstring for 10_Currency
# Congrats!
Woohoo! You learned variables in Python! 🙌

Here's a recap of everything we learned in this chapter:

Data types: int, float, str, bool.
Arithmetic operators: +, -, *, /.
The % modulo finds the remainder.
The ** exponentiation finds the exponent.
The input() function is used to get user input.
The int() function converts a value into an integer number.
Let's put it all together now!

Instructions
We just got home from a fun trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:

🇨🇴 Colombian pesos
🇵🇪 Peruvian soles
🇧🇷 Brazilian reais
Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

Make sure to Google the current exchange rates for pesos, soles, and reais!



The output should look something like this, but with different results:

What do you have left in pesos? 5600
What do you have left in soles? 105
What do you have left in reais? 280
413.0

The sequence should be:

Currency code example

Cha-ching! Now you have the total in USD. 💰

Once you are done, post a screenshot of your code to Twitter by clicking the icon below, and then head over to #CodedexCurrency and review another learner's work. Be supportive! :)



"""
# Write code below 💖

pesos = int(input('What do you have left in pesos? : '))
soles = int(input('What do you have left in soles? : '))
reais = int(input('What do you have left in reais? : '))

# 0.00026 USD = 1 pesos
# 0.30 USD = 1 soles
# 0.19 USD = 1 reais

total = pesos * 0.00026 + 0.30*soles + 0.19*reais
print((total))