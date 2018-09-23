# Dictionaries are unordered lists. Variables hold references to these dictionaries, much like they do for lists.
#dictionary = {"color": "lime green", "animal": "dolphin", "game": "World of Warcraft"}

# Dictionaries are comprised of "key-value pairs", and we retrieve values by 'calling' its associated key.
# While the first item in a dictionary would be called using "dictionary[0]", there isn't a first item in a dictionary (it's unordered.)
# The only time order matters in a dictionary is determining if two dictionaries are equal. (Equal means 'same'.)

# Keys can't be sliced like lists since they don't possess order.

# KeyErrors appear when the developer reference a key that doesn't exist in the dictionary.

# keys(), values(), and items() all return list-like data types, but it's important to note that these returned data types are not TRUE lists.
# They are not true lists because they do not have an append() method, and cannot be modified.
# Now, these returned data types, "dict_keys", "dict_values", and "dict_items", can all be used in for loops.
#for k in dictionary.values():
#    print(k)
# A very simple for loop that iterates over the values in a dictionary. You could use dict.keys() to iterate over its keys instead, or dict.items() to iterate over its key-value pairs.

# dict.items() returns a tuple instead of a list. If you want a list out of these returned values, they can be passed to the list() function for conversion.

# Testing a key OR value for existence in a dictionary can be done with the same operators as lists: "in" or "not in". These operators can be used on the dictionary value itself, and never has
# to be supplied with the dict.items() method.

# Accessing a key before we know its value is an arduous process, and therefore Python dictionaries are supplied with a "get()" method. The get() method accepts two arguments:
# 1) The key of the value to retrieve
# 2) A fallback value to return if that key doesn't exist
desserts = {"Cake": 10, "Pie": 8, "Pudding": 2, "Candy": 90}
# Now, the get() method can be used to return a key's value, should it exist, or something else if it doesn't. Let's say I want to announce the amount of pies I'm bringing to a get-together:
#print(desserts.get('Pie', 0)) # This looks for the "Pie" key in the dictionary, returns its value (if it exists), but will return 0, if not.
#print(desserts.get('Cookies', 0)) # This looks for the "Cookies" key in the dictionary, but will return 0 because that key doesn't exist.
# The get() method gracefully allows us to check for non-existing values in an elegant manner.

# The setdefault() method allows you to change the value of a key, only if that key doesn't already have a value.
desserts.setdefault("Ice Cream", 40)
print(desserts)
# The setdefault() method is a nice shortcut for checking key existence, and then setting a key's value if the key doesn't exist.
