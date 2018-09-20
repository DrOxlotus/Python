##
# Purpose: This is a simple implementation of a password manager.
##

#! python3

import sys, pyperclip

ACCOUNTS = {
    "facebook": "28EpJqpNUxHp8o8o9agSbNUz",
    "twitter": "AIqXg09nfIQhgAyzfDFNXgdT",
    "instagram": "wOwZwl0Jf8TP9o9X6olbBvIE",
    "gmail": "zHD17t8PhePZyq00cBqpBYYL"
}

if len(sys.argv) < 2:
    print("Usage: PasswordMgr.py <account_name>")
    sys.exit(0)

acc = sys.argv[1] # This sets 'acc' equal to the account name. (aka 'the key')

if acc in ACCOUNTS:
    pyperclip.copy(ACCOUNTS[acc])
    print("The password for " + acc + " has been copied to your clipboard.")
else:
    print(acc + " doesn't exist in your vault.")
