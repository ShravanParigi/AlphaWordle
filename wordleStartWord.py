f = open("WordsSpaced.txt", 'r')
h = open("WordleAnswers.txt", 'r')
g = open("WordsOutput.txt", 'r')

wordlistP = []
for x in f:
    wordlistP.append(x)

wordlistA = []
for x in h:
    wordlistA.append(x)

guessType = input("Guess Type (leastb, graded, categ): ")


#wordlistP = ["crane", "trace", "stare", "orate", "aurei", "rates", "squid"]

count = 100000
countg = 0
countc = 0
grade = 100000000
wordToGuess = ""
bestWords = []
for word in wordlistP:
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
        grade2 = 0
        categs = [0,0,0,0,0]
        for key in dictOutput:
            grade2 += dictOutput[key]
            grade2 += dictOutput[key]
            categs[0] +=1
            if dictOutput[key] > 2:
                grade2 -= dictOutput[key]
                categs[0] -=1
                categs[1] +=1
            if dictOutput[key] > 13:
                grade2 += dictOutput[key]
                categs[1] -=1
                categs[2] +=1
            if dictOutput[key] > 45:
                grade2 += dictOutput[key]
                categs[2] -=1
                categs[3] +=1
            if dictOutput[key] > 150:
                categs[3] -=1
                categs[4] +=dictOutput[key]
                grade2 += dictOutput[key]
        if grade2 < 5900:
            bestWords.append(word[:5])
            print(word[:5])
            print(str(categs) + str(len(dictOutput)))
            print(str(grade2))
            print()
        if grade2 < grade:
            grade = grade2
            wordToGuess = word
        elif grade2 == grade:
            if "ggggg" in dictOutput:
                wordToGuess = word
        

for w in bestWords:
    print(w)
print()
print("\n" + wordToGuess)
print(str(grade))

