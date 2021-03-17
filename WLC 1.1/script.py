import time
import os
from wlc import wdlist
from wlc import clear

def banner():
    clear()
    print("WordList Creator v1.1")
    time.sleep(3)
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
    time.sleep(2)
    clear()

def credits():
    print("""
                   +------------------------------+
                   | COPYRIGHT Daniel Falkov 2021 |
                   +------------------------------+
""")
    input("Press Enter to continue...")

def main():
    print("""
                          █ ▄▀█  █▀▄ █
                         ▐▌          ▐▌
                         █▌▀▄  ▄▄  ▄▀▐█
                        ▐██  ▀▀──▀▀  ██▌
                       ▄████▄  ▐▌  ▄████▄
                            4N0NYM0U5
                                                        
""")
    select = input("""
            Select an option:
               +---------------------------------+
               | 1 | Create wordlist             |
               +---------------------------------+
               | 2 | Read the wordlist.txt file  |
               +---------------------------------+
               | 3 | Credits                     |
               +---------------------------------+ 
               | Q | Quit                        |
               +---------------------------------+
            
 > """)
    if select == "1":
        clear()
        wdlist()
        main()
    elif select == "2":
        clear()
        f = open("wordlist.txt", "r")
        print(f.read())
        input("Press Enter to continue...")
        clear()
        main()
    elif select == "3":
        clear()
        credits()
        clear()
        main()
    elif select == "q" or select == "Q" or select == "quit" or select == "Quit":
        clear()
        quit()
    else:
        clear()
        main()

banner()
main()