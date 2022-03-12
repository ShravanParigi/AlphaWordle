f = open("WordsSpaced.txt", 'r')
h = open("WordleAnswers.txt", 'r')
g = open("WordsOutput.txt", 'w')

wordlist = []
for x in h:
    wordlist.append(x)

print("type word followed by a space followed by color combo")
print("  b for black or character not found")
print("  y for yellow or character found but wrong spot")
print("  g for green or character found in right spot")
print("e.g. word: stare bbygb")

# gb means only one instance of letter
# gg gy yg yy means atleast 2 instances of letter
# yb means only one instance of letter
# by means only one instance of letter
# bg means only one instance of letter

while(len(wordlist) != 1):
    word = input("word: ")
    if(word == "print"):
        for word in wordlist:
            print(word[:5], file = g)
        break
    for l in range(4):
        for c in range(4-l):
            if word[l] == word[c+l+1]:
                if (word[l + 6] != "b") & (word[c+l+7] != "b"):
                    templist = wordlist.copy()
                    for w in wordlist:
                        found = 0
                        for k in w:
                            if(k == word[l]):
                                found += 1
                        if found < 2:
                            templist.remove(w)
                    wordlist = templist.copy()
                elif (word[l + 6] != "b") | (word[c+l+7] != "b"):
                    templist = wordlist.copy()
                    if word[l + 6] == "g":
                        eword = list(word)
                        eword[c + l + 7] = str(l)
                        word = "".join(eword)
                    elif word[c +l + 7] == "g":
                        eword = list(word)
                        eword[l + 6] = str(c+l+1)
                        word = "".join(eword)
                    else:
                        eword = list(word)
                        eword[l + 6] = "y"
                        eword[c + l + 7] = "y"
                        word = "".join(eword)

                    for w in wordlist:
                        found = 0
                        for k in w:
                            if(k == word[l]):
                                found += 1
                        if found > 1:
                            templist.remove(w)
                    wordlist = templist.copy()
    for x in range(5):
        letter = word[x]
        color = word[x+6]
        templist = wordlist.copy()
        if(color == "b"):
            for w in wordlist:
                found = False
                for c in w:
                    if(c == letter):
                        found = True
                if found:
                    templist.remove(w)
            wordlist = templist.copy()
        elif (color == "y"):
            for w in wordlist:
                found = False
                for c in w:
                    if(c == letter):
                        found = True
                if(not found):
                    templist.remove(w)
            wordlist = templist.copy()
            for w in wordlist:
                if(w[x] == letter):
                    templist.remove(w)
            wordlist = templist.copy()
        elif (color == "g"):
            for w in wordlist:
                if(w[x] != letter):
                    templist.remove(w)
            wordlist = templist.copy()
        else:
            if (word[int(color) + 6] == "g"):
                for w in wordlist:
                    found = False
                    for c in range(5):
                        if(w[c] == letter) & (c != int(color)):
                            found = True
                    if found:
                        templist.remove(w)
                    wordlist = templist.copy()
    if(len(wordlist) == 1):
        print("The word is")
    else:
        print("There are "+ str(len(wordlist)) + " words left")
    if(len(wordlist) < 15):
        for word in wordlist:
            print(word[:5])




    

