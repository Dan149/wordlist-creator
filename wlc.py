import os

def color():
    if os.name =="nt":
        os.system("color 0A")
    else:
        pass
def clear():
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")

def wdlist():
    again = ""
    wordlist = []
    pin = []
    zero = ["0", "00", "000"]
    zero_to_hundred = []
    zero_to_thousand = []
    zero_to_ten_thousands = []
    for zh in range(100):
        zh_str = str(zh)
        zero_to_hundred.append(zh_str)
    for zt in range(1000):
        zt_str = str(zt)
        zero_to_thousand.append(zt_str)
    for ztt in range(10000):
        ztt_str = str(ztt)
        zero_to_ten_thousands.append(ztt_str)
    t = 0
    word_count = 0
    print("Tip: write only in lowercase letters, WLC will automatically do changes to it.\n\n-------------------------------------------------------")
    word = input("\nAdd a word: ")
    if word != "":
        wordlist.append(word)
        word_count += 1
        clear()
    else:
        clear()
        print("ERROR: words must have at least one letter.")
        wdlist()
    while again != "$ok":

        print(f"Amount of words: {word_count}.\n")
        print("To end the wordlist, type: $ok.\n\n-------------------------------------------------------")
        word = input("\nAdd a word: ")
        again = word
        if word != "":
            wordlist.append(word)
            word_count += 1
            clear()
        else:
            clear()
            print("ERROR: words must have at least one letter.")
    symbols = input("Include symbols ? Slower to generate, bigger file's size. [y/n]: ")
    if symbols == "yes" or symbols == "y":
        put_symb = True
    elif symbols == "no" or symbols == "n":
        put_symb = False
    else:
        print("ERROR: unexpected input.")
        quit()
    print("WORKING, PLEASE WAIT...")

    wordlist.pop()
    f = open("wordlist.txt", "w")
    f.close

    for m in range(len(wordlist)):
        word_lst = list(wordlist[m])
        if word_lst[0] == "a":
            word_lst.pop(0)
            word_lst.insert(0, "A")
        elif word_lst[0] == "b":
            word_lst.pop(0)
            word_lst.insert(0, "B")
        elif word_lst[0] == "c":
            word_lst.pop(0)
            word_lst.insert(0, "C")
        elif word_lst[0] == "d":
            word_lst.pop(0)
            word_lst.insert(0, "D")
        elif word_lst[0] == "e":
            word_lst.pop(0)
            word_lst.insert(0, "E")
        elif word_lst[0] == "f":
            word_lst.pop(0)
            word_lst.insert(0, "F")
        elif word_lst[0] == "g":
            word_lst.pop(0)
            word_lst.insert(0, "G")
        elif word_lst[0] == "h":
            word_lst.pop(0)
            word_lst.insert(0, "H")
        elif word_lst[0] == "i":
            word_lst.pop(0)
            word_lst.insert(0, "I")
        elif word_lst[0] == "j":
            word_lst.pop(0)
            word_lst.insert(0, "J")
        elif word_lst[0] == "k":
            word_lst.pop(0)
            word_lst.insert(0, "K")
        elif word_lst[0] == "l":
            word_lst.pop(0)
            word_lst.insert(0, "L")
        elif word_lst[0] == "m":
            word_lst.pop(0)
            word_lst.insert(0, "M")
        elif word_lst[0] == "n":
            word_lst.pop(0)
            word_lst.insert(0, "N")
        elif word_lst[0] == "o":
            word_lst.pop(0)
            word_lst.insert(0, "O")
        elif word_lst[0] == "p":
            word_lst.pop(0)
            word_lst.insert(0, "P")
        elif word_lst[0] == "q":
            word_lst.pop(0)
            word_lst.insert(0, "Q")
        elif word_lst[0] == "r":
            word_lst.pop(0)
            word_lst.insert(0, "R")
        elif word_lst[0] == "s":
            word_lst.pop(0)
            word_lst.insert(0, "S")
        elif word_lst[0] == "t":
            word_lst.pop(0)
            word_lst.insert(0, "T")
        elif word_lst[0] == "u":
            word_lst.pop(0)
            word_lst.insert(0, "U")
        elif word_lst[0] == "v":
            word_lst.pop(0)
            word_lst.insert(0, "V")
        elif word_lst[0] == "w":
            word_lst.pop(0)
            word_lst.insert(0, "W")
        elif word_lst[0] == "x":
            word_lst.pop(0)
            word_lst.insert(0, "X")
        elif word_lst[0] == "y":
            word_lst.pop(0)
            word_lst.insert(0, "Y")
        elif word_lst[0] == "z":
            word_lst.pop(0)
            word_lst.insert(0, "Z")
        text = ""
        for x in word_lst:
            text += x
        word_str = text
        wordlist.append(word_str)

        if put_symb == True:
            for s in range(len(wordlist)):
                object = "#" + wordlist[s]
                object2 = wordlist[s] + "#"
                object3 = "&" + wordlist[s]
                object4 = wordlist[s] + "&"
                object5 = "!" + wordlist[s]
                object6 = wordlist[s] + "!"
                object7 = "?" + wordlist[s]
                object8 = wordlist[s] + "?"
                wordlist.append(object)
                wordlist.append(object2)
                wordlist.append(object3)
                wordlist.append(object4)
                wordlist.append(object5)
                wordlist.append(object6)
                wordlist.append(object7)
                wordlist.append(object8)
        else:
            pass



    for p in range(len(wordlist)):
        transit = wordlist[p]
        word_upcase = transit.upper()
        wordlist.append(word_upcase)

    for y in range(10000):
        str_y = str(y)
        pin.append(str_y)

    for i in range(len(wordlist)):
        f = open("wordlist.txt","a")
        object = wordlist[i]
        object1 = "abc" + wordlist[i]
        object2 = wordlist[i] + "abc"
        f.write(object)
        f.write("""
""")
        f.write(object1)
        f.write("""
""")
        f.write(object2)
        f.write("""
""")
        for t in range(10000):
            objectpin1 = wordlist[i] + pin[t]
            objectpin2 = pin[t] + wordlist[i]
            f.write(objectpin1)
            f.write("""
""")
            f.write(objectpin2)
            f.write("""
""")
        for z in range(len(zero)):
            for zn in range(len(zero_to_hundred)):
                object_zero1 = wordlist[i] + zero[z] + zero_to_hundred[zn]
                object_zero2 = zero[z] + zero_to_hundred[zn] + wordlist[i]
                f.write(object_zero1)
                f.write("""
""")
                f.write(object_zero2)
                f.write("""
""")
            for n in range(len(zero_to_thousand)):
                object_zero3 = wordlist[i] + zero[z] + zero_to_thousand[n]
                object_zero4 = zero[z] + zero_to_thousand[n] + wordlist[i]
                f.write(object_zero3)
                f.write("""
""")
                f.write(object_zero4)
                f.write("""
""")
            for r in range(len(zero_to_ten_thousands)):
                object_zero5 = wordlist[i] + zero[z] + zero_to_ten_thousands[r]
                object_zero6 = zero[z] + zero_to_ten_thousands[r] + wordlist[i]
                f.write(object_zero5)
                f.write("""
""")
                f.write(object_zero6)
                f.write("""
""")

    f.close
    clear()


def testbox():
    print("Testbox (beta)")
    #example()
    #put your test function here
    input("\nPress Enter to return to the main menu...")
