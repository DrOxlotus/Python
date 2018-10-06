##
# Purpose: Searches strings for any characters that match the compiled regex pattern for a phone number or e-mail address.
##

from imports import *

phoneNumberPattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

emailPattern = re.compile(r"(\w+(.)?\w+)@(\w+).(\w+)")

search = phoneNumberPattern.search("My phone number is: 999-999-9999")
emailSearch = emailPattern.search("My email is: test.group@gmail.com")
print("A phone number was discovered! " + search.group())
print("An email was discovered! " + emailSearch.group())
