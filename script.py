import time
import os
from wlc import wdlist
from wlc import clear
from wlc import color
from wlc import testbox

def banner():
    clear()
    print("WordList Creator stable")
    time.sleep(1)
    print("""
                      +--------------------+
                      |    █ ▄▀█  █▀▄ █    |
                      |   ▐▌          ▐▌   |
                      |   █▌▀▄  ▄▄  ▄▀▐█   |
                      |  ▐██  ▀▀  ▀▀  ██▌  |
                      | ▄████▄  ▐▌  ▄████▄ |
                      +--------------------+
                          -DUMBCHICKEN-
""")

    time.sleep(2.5)
    clear()

def credits():
    print("""
                     +-------------------------------------------------------------+
                     | © DumbChicken (Dan149 on Github) 2021, all rights reserved. |
                     +-------------------------------------------------------------+
""")
    input("Press Enter to continue...")

def main():
    print("""
             /$$      /$$      /$$            /$$$$$$
            | $$  /$ | $$     | $$           /$$__  $$
            | $$ /$$$| $$     | $$          | $$  \__/
            | $$/$$ $$ $$     | $$          | $$
            | $$$$_  $$$$     | $$          | $$
            | $$$/ \  $$$     | $$          | $$    $$
            | $$/   \  $$     | $$$$$$$$    |  $$$$$$/
            |__/     \__/ord  |________/ist  \______/reator

""")
    select = input("""
            Select an option:
               +---+-----------------------------+
               | 1 | Create Word-List            |
               +---+-----------------------------+
               | 2 | Read the wordlist.txt file  |
               +---+-----------------------------+
               | 3 | Credits                     |
               +---+-----------------------------+
               | Q | Quit                        |
               +---+-----------------------------+

WLC > """)
    if select == "1":
        clear()
        wdlist()
        print("Successfully saved data in wordlist.txt file.")
        main()
    elif select == "2":
        clear()
        verify = os.path.exists("wordlist.txt")
        if verify == True:
            f = open("wordlist.txt", "r")
            print(f.read())
            f.close
        else:
            print("ERROR: wordlist.txt doesn't exist.")
        input("Press Enter to continue...")
        clear()
        main()
    elif select == "3":
        clear()
        credits()
        clear()
        main()
    elif select == "testbox":
        warning = input("Warning: This is a testing zone that helps the developer testing new features.\n Do you want to continue ? [y/n]\n WLC > ")
        if warning == "yes" or warning == "y" or warning == "Yes" or warning == "Y":
            clear()
            testbox()
            clear()
            main()
        else:
            clear()
            main()
    elif select == "Q" or select == "quit" or select == "Quit":
        clear()
        [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]
        [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]
        quit()
    else:
        clear()
        main()
color()
banner()
main()
