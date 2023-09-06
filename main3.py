from bintreeFile import Bintree


svenska = Bintree()
with open("word3.txt", "r", encoding="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            None
        else:
            svenska.put(ordet)
print("\n")


engelska = Bintree()
with open("engelska.txt", "r", encoding="utf-8") as engelskafil:
    for line in engelskafil:
        words = line.split()
        for word in words:
            word = word.strip(".,!?\"'()[]{}")
            if word in engelska:
                None
            else:
                engelska.put(word)
                if word in svenska:
                    print(word)
print("\n")
