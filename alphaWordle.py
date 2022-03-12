f = open("WordsSpaced.txt", 'r')
h = open("WordleAnswers.txt", 'r')
g = open("WordsOutput.txt", 'w')



wordlistP = []
for x in f:
    wordlistP.append(x)

wordlist = []
for x in h:
    wordlist.append(x)



print("type the color combo")
print("  b for black or character not found")
print("  y for yellow or character found but wrong spot")
print("  g for green or character found in right spot")
print("e.g. word: stare bbygb")
word = "trace "
print('Guess "'+word[:5]+'"')

while(len(wordlist) != 1):
    word += input("color combo: ")
    # if(word == "print"):
    #     for word in wordlist:
    #         print(word[:5], file = g)
    #     break
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
    
    print("There are "+ str(len(wordlist)) + " possible words")
    if((len(wordlist) < 15) & (len(wordlist) > 1)):
        for word in wordlist:
            print(word[:5])

    if(len(wordlist) > 2): 
        countc = 0
        wordToGuess = ""
        print("")
        print("Calculating word to guess")
        wcount = 0
        for w in wordlistP:
            wcount +=1
            if(wcount == 2000):
                print("25%")
            if(wcount == 4000):
                print("50%")
            if(wcount == 6000):
                print("75%")
            if(wcount == 8000):
                print("100%")
                print("")
            dictOutput = {}
            dictOutput.update({"bbbbb": 0})
            countg2 = 0
            for w2 in wordlist:
                colors = ""
                for e in range(5):
                    cl = "b"
                    for d in range(5):
                        if w[e] == w2[d]:
                            if e == d:
                                cl = "g"
                            elif cl == "b":
                                cl = "y"
                    colors = colors + cl
                if colors not in dictOutput:
                    dictOutput.update({colors: 1})
                else:
                    dictOutput[colors] += 1
            if  dictOutput["bbbbb"] == 0:
                dictOutput.pop("bbbbb")
            countc2 = len(dictOutput.keys())

            if countc2 > countc:
                countc = countc2
                wordToGuess = w
            elif countc2 == countc:
                if "ggggg" in dictOutput:
                    countc = countc2
                    wordToGuess = w
    else:
        wordToGuess = wordlist[0]
    if len(wordlist) > 1:
        print('Guess "'+ wordToGuess[:5] + '"')
    else: 
        print('The word is "'+ wordToGuess[:5] + '"')
    word = wordToGuess[:5] + " "
    




    

