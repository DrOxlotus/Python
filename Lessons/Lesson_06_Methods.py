list = ['Alex', 'bees', 'Broach', 'elephant', 'Eerie', 'rat', 'bat', 'cat', 'bird', 'dog']
#print(list.index('bat')) (Fetches the index of 'bat' in the list)

#list.append('goose') (Adds 'goose' to the end of the list)
#print(list)

#list.insert(1, 'moose') (Adds 'moose' as the second value in the list)
#print(list)

#list.remove('cat') (Removes 'cat' from the list -- helpful if you don't know the index of cat, or if the index changes)
#print(list)

# The sort() method sorts lists in place, and therefore doesn't return a sorted list. (list = list.sort() wouldn't hold anything.)
# The sort() method can't sort alphanumerical lists. (Throws a TypeError.)
# The sort() method uses ASCIIbetical order, and not a *true* alphabetical order.
# -----------------------
#list.sort() (Puts this list in ASCIIbetical order)
#list.sort(reverse = True) (Puts the list in reversed ASCIIbetical order)
#print(list)

# It's worth noting that indexing, slicing, len(), and the 'in' and 'not in' operators all function on strings since they're a list-like type.
# The difference between strings and lists is their mutability. In other words, strings are immutable (can't be changed), while lists are mutable (can be changed).

# Use 'slicing' and 'concatenation' to "mutate" strings. (This process will create a *new* string!)

# Modifying lists must be done using its associated methods. Using "list = [1, 2, 3] and list = [4, 5, 6]" will actually cause the first version of the list to be overwritten by the second.
# Combo'ing del() and append() together won't overwrite the list; it will CHANGE the original list by wiping the original values first, and then adding the new ones.

# Tuples are list-like data types, except in two ways:
# 1) Tuples are syntactically typed with parentheses instead of square brackets. "list = ('pie', 'cake', 'candy')"
# 2) Tuples are immutable. (Attempting to append, remove, or modify items in a tuple will throw a TypeError exception.)
# If you have a single value in your tuple, you must use a trailing comma, or Python won't know it's supposed to be a tuple.
#tuple = ('pie',)
#print(type(tuple)) (Returns <class 'tuple'>)
# USE CASE: Tuples are used when the developer(s) need an ordered sequence of values that aren't intended to be changed. ("A *sequence of constants*".)
