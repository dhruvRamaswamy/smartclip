#! python3.10.4
# v1.0
# mcb.py
# Smart Copy and Paste, read the readme to find out other cool details
# use the 'help' command to get documentation

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

# Todo: save clipboard content
# Todo: List keywords and load content

# Saves clipboard content if the user uses the 'save' keyword
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        # Copies
        pyperclip.copy(str(list(mcbShelf.keys())))
    # If the command line argument is a keyword, load the value onto the clipboard
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()