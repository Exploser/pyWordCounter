#! python3
import pyperclip, pprint
import sys

text = pyperclip.paste()

charCounter = {}

def idvCharCounter():
    for char in text.lower():
        charCounter.setdefault(char,0)
        charCounter[char] += 1
    pprint.pprint(charCounter)
    return idvCharCounter

def wordCounter():
    wordCount = 0
    for i in range(len(text)):
        char = text[i]
        leng = len(text)
        if (i < (leng-1)):
             nextChar = text[i+1]
             if (char == ' ' and nextChar != ' '):
                wordCount += 1
        elif (i >= (leng-1)):
            wordCount += 1
    pprint.pprint("Word count = " + str(wordCount))

        
def totalCharCounter():
    totalCharCount = 0
    for char in text.lower():
        charCounter.setdefault(char,0)
        charCounter[char] += 1
        if(ord(char) >= 97 or ord(char) <= 122): #32 - 126
                totalCharCount += 1
                
    pprint.pprint("Character Count = " + str(totalCharCount))
    return totalCharCount

def handler():
    arg = sys.argv[1]
    
    if (len(sys.argv) > 2):
        print("Error Usage")
        helper()
    
    if (arg == '-c'):
        totalCharCounter()
    if (arg == '-i'):
        idvCharCounter()
    if (arg == '-w'):
        wordCounter()
    if (arg == '-h'):
        helper()

handler()