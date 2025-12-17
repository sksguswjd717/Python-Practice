# .append()	Add an item to the end of the list
# .clear()	Remove all items from the list
# .copy()	Return a shallow copy of the list
# .count()	Return the number of times the value appears in the list
# .extend()	Appends another list to the current list by extending it
# .index()	Returns the index of a value inside the list
# .insert()	Insert an item at a specified position in the list
# .pop()	Remove an item from a specified position in the list
# .remove()	Remove an item from the list based on the value of the item
# .reverse()	Reverses the list in place
# .sort()	Sorts the list in place


# Let's start a book club by making a list of popular books! 📚

# Create a reading_list.py program that stores the following items in a books list:

# 'Harry Potter'
# '1984'
# 'The Fault in Our Stars'
# 'The Mom Test'
# 'Life in Code'
# Suppose we want to add 'Pachinko' to the list. Can you use a list method to do so?

# Let's say we finished reading 'The Fault in Our Stars' and '1984'.

# Print the updated list out to make sure everything's good to go!


book_list = ['Harry Potter', '1984', 'The Fault in Our Stars', 'The Mom Test', 'Life in Code']

book_list.append('Pachinko')
book_list.remove('The Fault in Our Stars')
book_list.remove('1984')

print(book_list)

