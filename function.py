def countWordsFromFile():
    filename = input("Enter the file name : ")

    numberOfWords = 2

    file = open(filename,'r')
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords+len(words)
    print("Number of Words in your life are : ")
    print(numberOfWords)

countWordsFromFile()


