import os

def clear():
    if os.name =="nt": 
        os.system("cls")
    else:
        os.system("clear")

def wdlist():
    again = ""
    wordlist = []
    print("To end the wordlist, type: #stop#\n")
    word = input("Add a word: ")
    wordlist.append(word)
    clear()
    while again != "#stop#":
        print("To end the wordlist, type: #stop#\n")
        word = input("Add a word: ")
        again = word
        wordlist.append(word)
        clear()
    
    wordlist.pop()
    f = open("wordlist.txt", "w")
    f.close
    for i in range(len(wordlist)):
        f = open("wordlist.txt","a")
        object = "123" + wordlist[i]
        object2 = "1234" + wordlist[i]
        f.write(wordlist[i])
        f.write("""
""")
        f.write(object)
        f.write("""
""")
        f.write(object2)
        f.write("""
""")
    f.close
    input("Press Enter to continue...")