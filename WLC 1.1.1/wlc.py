import os

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
    input("Press Enter to continue...")
    clear()