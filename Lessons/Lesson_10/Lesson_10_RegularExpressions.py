from imports import *

### Matching Characters ###
# ? - Means the preceding group is optional _OR_ one is declaring a non-greedy match
# * - Means the preceding group can be absent or repeated many times, but it will still match
# + - Means the preceding group can be repeated many times, and will match, but it must appear at least once
# {} - Means to match a specific set of repetition
# ^ - Means that the match should be opposite of the character class _OR_ indicates that a match must occur at the beginning of the search parameter
# $ - Means that the match must occur at the end of the search parameter
# ^$ - Means that the entire search parameter must match the regex object
# . - Means that any character (except the newline character) will be matched (by default, it matches only one character)
# .* - Means that any and all characters (except the newline character) will be matched
    # This matching character set uses 'greedy' pattern searching. In other words, this will try and match as much text as possible
    # To match in a 'non-greedy' method, use the character set below
# .*? - Means that any and all characters (except the newline character) will be matched (non-greedy)

### Character Classes ###
# \d - Stands for any numeric digit (0|1|2|3|4|5|6|7|8|9)
# \D - Stands for any character that is NOT a numeric digit
# \w - Stands for any letter, numeric digit, or the underscore character
# \W - Stands for any character that is NOT a letter, numeric digit, or the underscore character
# \s - Stands for any space, tab, or newline character
# \S - Stands for any character that is NOT a space, tab, or newline character

### Good To Know ###
# re.compile(".*", re.DOTALL) - This will match everything, including the newline character
# re.compile(r"\w", re.IGNORECASE) - This will match any letter, whether it's lowercase or uppercase
"""
regex = re.compile(r"Instructor (\w)\w*")
regex.sub(r"\1********", "Instructor Josh gave a very poor evaluation of Instructor Bill.")
"""

"""
phoneNumberPattern = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
phoneNumberPattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
"""

try:
    """
    phoneNumberPattern = re.compile(r"\d{3}-\d{3}-\d{4}") # Compiles a Regex object to use for pattern matching
    search = phoneNumberPattern.search("My phone number is 123-456-7890!!!!!")
    print("A phone number was found: " + search.group()) # Returns the full match since we know the result isn't None

    #123-456-7890
    #1234567890
    #(123)-456-7890
    #123.456.7890

    phoneNumberPattern = re.compile(r"(\d{3})-(\d{3}-\d{4})")
    search = phoneNumberPattern.search("My phone number is 123-456-7890!!!!!")
    areaCode, mainChunk = search.groups() # The groups() method returns a Tuple object
    print(areaCode)

    phoneNumberPattern = re.compile(r"(\(\d{3}\))-(\d{3}-\d{4})") # This escapes an opening and closing parentheses set to show that they should match in the search string
    search = phoneNumberPattern.search("My phone number is (123)-456-7890!!!!!")
    print(search.group(1))

    phoneNumberPattern = re.compile(r"123-(\d{3}-\d{4})")
    search = phoneNumberPattern.search("Phone number(s): 123-466-7890")
    print(search.group())

    phoneNumberPattern = re.compile(r"(\(\d{3}\))?(.)?(-)?\d{3}(.)?(-)?\d{4}") # This MONSTROUS Regex object matches all four phone number patterns above.
    search = phoneNumberPattern.search("Phone number: (123).345.9898")
    print(search.group())

    phoneNumberPattern = re.compile(r"(\(\d{3}\))*(.)?(-)?\d{3}(.)?(-)?\d{4}")
    search = phoneNumberPattern.search("Phone number: (123).345.9898")
    print(search.group())

    phoneNumberPattern = re.compile(r"(\(\d{1,}\))?(.)?(-)?\d{1,}(.)?(-)?\d{1,}") # The {} allow us to define a static number, or even a range of numbers, which can be bound or unbound, to match instances
    search = phoneNumberPattern.search("Phone number: (123).345.9898")
    print(search.group())

    # This is known as "greedy pattern matching", and will always return the longest result
    # The return of the shortest result is known as "non-greedy pattern matching"
    greedyTextPattern = re.compile(r"(Alex){1,}")
    nonGreedyTextPattern = re.compile(r"(Alex){1,}?")
    greedySearch = greedyTextPattern.search("AlexAlexAlexAlexAlex")
    nonGreedySearch = nonGreedyTextPattern.search("AlexAlexAlexAlexAlex")
    print(greedySearch.group() + "\n" + nonGreedySearch.group())

    textPattern = re.compile(r"Alex('s Computer|'s Socks|'s Keyboard)")
    search = textPattern.search("Alex's Computer is next to Alex's Keyboard, and is above Alex's Socks.")
    print(search.group())

    findall = textPattern.findall("Alex's Computer is next to Alex's Keyboard, and is above Alex's Socks.")
    print(findall)

    # The findall() method returns a list of matched strings if no groups are used in the regex object, and will return a tuple of matched items if groups are used in the regex object
    phoneNumberPattern = re.compile(r"((\()?\d{3}(\))?)(.)?(-)?(\d{3}(.)?(-)?\d{4})")
    findall = phoneNumberPattern.findall("Phone numbers: (123).345.9898 123-455-2342 8018343321 (999)-999-9999")
    print(findall)

    regex = re.compile(r"\d+\s\w+")
    search = regex.search("There is 1 number here")
    print(search.group())

    vowelRegex = re.compile(r"[aeiouAEIOU]") # This line of code is building a custom character class, much like \d or \w
    findall = vowelRegex.findall("Regular expressions are VERY cool. I don't know what I would DO WITHOUT THEM!")
    print(findall)

    negatedVowelRegex = re.compile(r"[^aeiouAEIOU]") # This line of code is building a custom character class, but is negated, which means it will match anything NOT present in the square brackets []
    findall = negatedVowelRegex.findall("Regular expressions are VERY cool. I don't know what I would DO WITHOUT THEM!")
    print(findall)
    """

except AttributeError:
    print("Pattern not found.")
