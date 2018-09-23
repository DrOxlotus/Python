"""
var1 = 1
var2 = var1
var1 = 2
print(var1, var2)
"""
# The output above is "2 1" because var1 and var2 are separate variables that hold their own values.

# Lists don't function the same way. If you assign a list to a variable, you're actually assigning a LIST REFERENCE to the variable, and that reference points to the list.
"""
list = [1, 2, 3, 4, 5, 6]
anotherList = list
anotherList[0] = "Wut?"
print(list, anotherList)
"""
# When assigning anotherList to the value of list, what actually happened is the reference to the list was copied. Thus, 'list' and 'anotherList' reference the same bit of data somewhere in memory,
# and that's why the output of the above chunk of code may look funny.
# It's worth mentioning that Python uses unique ID values for lists, but they're used internally, and the developer should never need to worry about them.

# References are used on any MUTABLE data type in Python. (These are lists and dictionaries.) Immutable data types only ever use the value of something, opposed to a reference.
# REMEMBER: Don't confuse yourself with the colloquiallism ideology that variables hold list values and dictionaries as a whole, opposed to references. People say that variables hold the
# lists and dictionary values, but that's false, and they use a reference instead. (You can prove it using a few lines of code...and we did.)

# Passing references is important to understand because it helps us understand how function calls work internally.
# When a function is called, and we pass values to it, we don't pass the actual value, we pass a reference of the original value to the parameter variables.
"""
def Test(arg1):
    arg1.append("Ha!")

list = [1, 2, 3]
Test(list)
print(list)
"""
# It's worth mentioning that a return statement doesn't exist because that would overwrite the original list, opposed to a simple modification.
# Never forget that Python handles mutable data types (lists and dictionaries) using references instead of values. This element of Python slipping your mind can lead to some confusing bugs. (No fun!)

#------------------------------------

# Modifying a list is handy, and reference passing is a wonderful and powerful thing, but we don't always want the modified list to update the original list. There is a module in the
# standard library called "copy", and this module possesses two great functions to handle these situations: copy() and deepcopy().
"""
from copy import copy, deepcopy
list = [1, 2, 3, 4, 5]
anotherList = copy(list)
anotherList[0] = 0
print(list, anotherList)
"""
# copy() creates a full copy of the list/dictionary value, instead of a copied reference. Thus, we now have two SEPARATE lists.
# If the list has sublists, then you'll need to use deepcopy() instead of copy()
