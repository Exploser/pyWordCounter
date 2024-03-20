#!/usr/bin/python3
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

def helper():
    print('''The script accepts command-line arguments to specify the operation to perform:

    -c: Count total characters in the clipboard text that are within the ASCII range 97 to 122 (inclusive). Note: There seems to be a logical error in this range check, as it should be and instead of or to accurately filter characters.
    -i: Count the occurrences of each individual character in the clipboard text, ignoring case.
    -w: Count the total number of words in the clipboard text. A word is defined as any sequence of characters separated by whitespace.
    -h: Display help information using a function from an external module named helper.''')

        
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
    try:
        arg = sys.argv[1]
    except:
        print("No arguments passed?")
        helper()
        return

    if (len(sys.argv) > 2):
        print("Error Usage")
        helper()
    
    if (arg == '-c'):
        totalCharCounter()
    if (arg == '-i'):
        idvCharCounter()
    if (arg == '-w'):
        wordCounter()
    if (arg == '-h' or arg=='--h' or arg=='-help' or arg=='--help'):
        helper()

handler()