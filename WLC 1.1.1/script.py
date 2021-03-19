import time
import os
from wlc import wdlist
from wlc import clear

def banner():
    clear()
    print("WordList Creator v1.1.1")
    time.sleep(1)
    print("""
                          █ ▄▀█  █▀▄ █
                         ▐▌          ▐▌
                         █▌▀▄  ▄▄  ▄▀▐█
                        ▐██  ▀▀  ▀▀  ██▌
                       ▄████▄  ▐▌  ▄████▄
                            4N0NYM0U5
                         BELIEVE IN G0D.
""")
    
    time.sleep(4)
    clear()

def credits():
    print("""
                     +----------------------+
                     | © Daniel Falkov 2021 |
                     +----------------------+
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
    elif select == "q" or select == "Q" or select == "quit" or select == "Quit":
        clear()
        quit()
    else:
        clear()
        main()

banner()
main()