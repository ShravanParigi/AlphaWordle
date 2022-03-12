f = open("WordleWords.txt", 'r')
g = open("WordsSpaced.txt", "x")
for x in f:
    while(x != ""):
        word = x[:5]
        x = x[5:]
        g.write(word + "\n")
        while((x[0] >= "0" )&( x[0] <= "9")):
            x = x[1:]
        