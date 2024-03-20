#!/usr/bin/python3
import pyperclip
import sys

def print_help():

    help_text = """
    Usage: script.py [option]
    Options:
        -c  Count total characters (excluding spaces)
        -i  Count individual characters frequency
        -w  Count words
        -h  Show this help message
    Default action (no option provided): Count words
    """
    print(help_text)

def count_words(text):

    words = text.split()
    print(f"Word count = {len(words)}")

def count_characters(text):

    char_count = len([char for char in text if char.isalnum()])
    print(f"Character Count = {char_count}")

def count_individual_characters(text):
    
    char_counter = {}
    for char in text.lower():
        if char.isalnum(): # Counting only alphanumeric characters
            char_counter[char] = char_counter.get(char, 0) + 1
    for char, count in sorted(char_counter.items()):
        print(f"{char}: {count}")

def main():
    text = pyperclip.paste()
    
    option = sys.argv[1] if len(sys.argv) == 2 else '-w'

    if option == '-h':
        print_help()
    elif option == '-w':
        count_words(text)
    elif option == '-c':
        count_characters(text)
    elif option == '-i':
        count_individual_characters(text)
    else:
        print("Unknown option. Defaulting to word count.")
        count_words(text)

if __name__ == "__main__":
    main()
