f = open("WordsSpaced.txt", 'r')
h = open("WordleAnswers.txt", 'r')
g = open("WordsOutput.txt", 'r')

wordlistP = []
for x in f:
    wordlistP.append(x)

wordlistA = []
for x in g:
    wordlistA.append(x)

guessType = input("Guess Type (leastb, graded, categ): ")

count = 100000
countg = 0
countc = 0
wordToGuess = ""
for word in wordlistP:
    print(word[:5])
    dictOutput = {}
    dictOutput.update({"bbbbb": 0})
    countg2 = 0
    for word2 in wordlistA:
        colors = ""
        for c in range(5):
            letter = "b"
            for d in range(5):
                if word[c] == word2[d]:
                    if c == d:
                        letter = "g"
                    elif letter == "b":
                        letter = "y"
            colors = colors + letter
            if letter == "g":
                countg2 +=3
            elif letter == "y":
                countg2 +=1
        if colors not in dictOutput:
            dictOutput.update({colors: 1})
        else:
            dictOutput[colors] += 1
    if(guessType == "leastb"):
        count2 = dictOutput["bbbbb"]
        if count2 < count:
            count = count2
            wordToGuess = word
    elif(guessType == "graded"):
        if countg2 > countg:
            countg = countg2
            wordToGuess = word
    else:
        if  dictOutput["bbbbb"] == 0:
            dictOutput.pop("bbbbb")
        countc2 = len(dictOutput.keys())
        if countc2 > countc:
            countc = countc2
            wordToGuess = word
        elif countc2 == countc:
            if "ggggg" in dictOutput:
                countc = countc2
                wordToGuess = word
        


print("\n" + wordToGuess)
print(str(countc))

