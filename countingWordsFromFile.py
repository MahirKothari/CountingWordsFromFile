def countingWordsFromFile():
    fileName = input('enter file name')
    f = open(fileName,'r')
    numberOfWords = 0
    for line in f:
        words = line.split()
        numberOfWords = numberOfWords+len(words)
        
    print(numberOfWords)
countingWordsFromFile() 
