#! python3.10.4
# v2.0
# mcb.py
# Smart Copy and Paste, read the readme to find out other cool details
# i didn't add any comments yet, that is for in a few days anyway
# u can see all the todos, more to come and more to be finished
import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')


# Todo: Add so that a file can be added
# Todo: Add list of key and values
# Todo: Add keywords/values via clipboard
# Todo: Add clear/delete functionality
# Todo: Solve the keys problem
print("Welcome to dhruvclip! Enter 'cmds' to get a list of commands used, as well as 'docs' for documentation and 'exit' to exit!")
# Saves clipboard content if the user uses the 'save' keyword
end = False
while not end:
    keyword = input('>>> ')
    if keyword[0] == '#':
        term = keyword[1:]
        try:
            stuffThatWillBePutOnClipboard = mcbShelf[term]
            pyperclip.copy(stuffThatWillBePutOnClipboard)
        except KeyError:
            print("Key wasn't found")
            continue
        except:
            print("Something went wrong...")
            continue
        else:
            print("Success")

    elif keyword == "add":
        print("Enter a keyword")
        newKeyword = input(">>> ")
        if newKeyword in mcbShelf.keys():
            print("Error, you entered a keyword that already exists. Enter 'currentks' to get all current keys")
            continue
        if newKeyword[0] == '#':
            print("Error, your keyword cannot start with '#'")
            continue
        print("Enter a Value")
        newValue = input(">>> ")
        try:
            mcbShelf[newKeyword] = newValue
        except:
            print(f"Something went wrong")
            continue
        else:
            print("Added value was a success")
            continue
    elif keyword == "currentks":
        print(f"{mcbShelf.keys()} lol inita solve this")
    elif keyword == "cmds":
        print("""
        Lol i don't have much rn
        \nadd: adds a keyword but you can't use '#' at the start
        \nexit: exits the program
        \ncurrentks: gets all current keys  
        \nto access a value type in '#' and the keyword ( #insertkeyhere )
        """)

    elif keyword == 'exit':
        end = True
    else:
        print("Error: Not a valid command. Enter 'cmds' to get a list of commands/documentation")
mcbShelf.close()
