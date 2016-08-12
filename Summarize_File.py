#Summarize_File.py
#Takes in a text file and writes a summary of that file to both the terminal and to a file

from pprint import pprint
import os.path, time, sys

print("What is the name of your file?")
inputFileName = input()
if(not os.path.isfile(inputFileName)):
    sys.exit("Not a file in this directory")

with open(fileName+'_summary.txt','w') as summary:
    summary.write("Summary for " + fileName+":\n")
    print("File created at :" + str(time.ctime(os.path.getctime(fileName))))
    print("File modified at :" + str(time.ctime(os.path.getmtime(fileName))))
    pprint("File created at :" + str(time.ctime(os.path.getctime(fileName))), stream=summary)
    pprint("File modified at :" + str(time.ctime(os.path.getmtime(fileName))), stream=summary)
    pprint("\n", stream=summary)
    print("\n")

    #NumLines analysis
    #with open(inputFileName, 'r') as f:
    #    for numLines, l in enumerate(f):
    #        pass
    #    numLines=numLines+1


    #Lines and Words analysis
    numLines = 0
    numWords = 0 
    uniques = {}
    with open(inputFileName, 'r') as f:
        for line in f:
            numLines = numLines + 1

            words = line.split()
            numWords = numWords + len(words)

            for currentWord in words:
                if currentWord in uniques:
                    uniques[currentWord] = uniques[currentWord] + 1
                else:
                    uniques[currentWord] = 1


    #NumChars analysis


    #Printing
    print("Lines: " + str(numLines))
    pprint("Lines: " + str(numLines), stream=summary)

    print("Words: " + str(numWords))
    pprint("Words: " + str(numWords), stream=summary)

    print("Unique words: " + str(len(uniques)))
    pprint("Unique words: " + str(len(uniques)), stream=summary)

    #print("Characters: " + str(numChars))
    #pprint(numChars, stream=summary)

    pprint("\n", stream=summary)
    print("\n")

    #Character anaylsis
    charDict = {}
    with open(inputFileName, 'r') as f:
        for line in f:
            for currentChar in line:
                if currentChar in charDict:
                    charDict[currentChar] = charDict[currentChar] + 1
                else:
                    charDict[currentChar] = 1
        pprint(charDict, stream=summary)
    pprint(charDict)
