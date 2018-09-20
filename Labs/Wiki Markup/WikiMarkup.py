##
# Purpose: Automate creating unordered lists for wikis.
##

# Source: https://en.wikipedia.org/wiki/List_of_lists_of_lists

import sys, pyperclip

clipboard = pyperclip.paste()

if clipboard == "" or None:
    print("Your clipboard is empty.")
    sys.exit(1)
else:
    temp = "" # Used to create the proper markup output for the clipboard variable
    for line in clipboard.split("\n"):
        temp = temp + "* " + line + "\n"

    clipboard = temp # Now that I have the proper markup output, let's make sure that the clipboard variable holds that new value
    pyperclip.copy(clipboard) # Copy the new formatted output to Windows' clipboard
