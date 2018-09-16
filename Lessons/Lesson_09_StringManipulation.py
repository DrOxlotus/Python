"""
Lesson Projects:
- (Simple) Password Manager
- Text Formatting Automation
"""

# There are several ways to write, print, and access strings in Python.
### STRING LITERALS ###
    ## Single/Double Quotes ##
#print('I like ice cream.')
#print("That is Tom's computer!")
    ## Escape Characters ##
    # Note: These are commonly referred to as "escape sequences." They consist of a backslash (\) and the character desired in the string.
    # Example: \' would add a single quote to the string.
#print('That is Tom's computer') # This is very bad, and will cause a SyntaxError to be thrown.
#print('That is Tom\'s computer!')

"""
    \' -> Single Quote
    \" -> Double Quote
    \t -> Tab
    \n -> New line
    \\ -> Backslash
"""

#print("Hi, Oxlotus!\nHow are you today?\n\tI'm your Python code, and I'm just swell!")

    ## Raw Strings ##
    # Note: Raw strings ignore all escape sequences in a string, and will print any and all backslashes present in the literal. All you need is an 'r' in front of the literal.
#print(r"Hi, Oxlotus!\nHow are you today?\n\tI'm your Python code, and I'm just swell!")

    # Raw strings can be very helpful whenever string literals contain many backslashes; print the raw form to read the literal and help yourself debug, if necessary.
    # These are very helpful when using regular expressions.

    ## Multiline Strings w/ Triple Quotes ##
    # Note: You could use the '\n' escape sequence each time a new line is required; however, multiline strings are often much simpler and save time.
#print("""Dear Oxlotus,
#
#Thank you very much for this short tutorial
#
#Yours Forever,
#COM-PUU-TOR
#""")

    # There's no need to escape anything, and code block indentation rules don't apply to multiline strings.

    ## Multiline Comments ##
    # Note: The hash (#) character denotes the beginning of a comment to the end of the same line.
    # We use multiline strings for comments that span multiple lines. (It's really not the best thing in the world, and I really, really hope that they change it.)
    # You can find an example of a multiline comment in previous lessons, as well as up above.

### INDEXING AND SLICING STRINGS ###
    # Note: Strings use indicies and slices just like the list data type.
    # The reason for that is because strings are much like a list of characters, and each character possesses an index in the list.
#greeting = "Hi, Oxlotus!"
#for i in enumerate(greeting):
#    print(i)

### THE 'IN' AND 'NOT IN' OPERATORS AND STRINGS ###
    # Note: As previously stated, strings are much like lists; therefore, the 'in' and 'not in' operators work on strings.
#print("Hi" in "Hi, Oxlotus!") # Returns True

### USEFUL STRING METHODS ###
    ## upper(), lower(), isupper(), and islower() String Methods ##
#greeting = "Hi, Oxlotus!"
#print(greeting + " " + greeting.upper() + " " + greeting.lower())
        # The methods used above DO NOT change the original string, but return a NEW string instead.
        # If you want to change the original string, then the methods must be called and stored in the original variable.
        # Example: greeting = greeting.upper()

        # The isupper() and islower() methods are Boolean methods that return True only if all characters are uppercase or lowercase, respectively, and return False otherwise.

"""
    - isalpha(): Returns True if the string contains ONLY letters, and isn't blank.
    - isalnum(): Returns True if the string contains ONLY numbers and letters, and isn't blank.
    - isdecimal(): Returns True if the string contains ONLY numeric characters, and isn't blank.
    - isspace(): Returns True if the string contains ONLY spaces, tabs, and new lines, and isn't blank.
    - istitle(): Returns True if the string contains ONLY words that start with uppercase letters followed by lowercase letters.
"""

        # All of the above methods are very helpful when user input validation is in question.

### THE startswith() AND endswith() STRING METHODS ###
    # Note: These are Boolean methods that return True if the string they're called on starts with or ends with the string passed to the method, respectively.
#print("Test".startswith("T"))
#print("Oxlotus".endswith("F"))

### THE join() AND split() STRING METHODS ###
    # Note: The join() method is useful when multiple strings need to be brought together.
    # The join() method is called on a string, is passed a list of strings, and then returns a new string.
#print(", ".join(["Tom", "Jodi", "Rick", "Sarah"]))
    # The string the join() method is called on is inserted between each item in the list.

    # The split() method is the exact opposite of the join() method. This method is called on a string, but returns a list of strings.
#print("Hi, Oxlotus!".split())

    # By default, the split() method scans for whitespace, tabs, or new lines to split the string on. You can pass a 'delimiter', or a different character, to split on.
    # Common Delimiters: "," - ":"

### JUSTIFYING TEXT WITH rjust(), ljust(), AND center() METHODS ###
