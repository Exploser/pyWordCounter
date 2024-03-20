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
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments.")
        print_help()
        return

    option = sys.argv[1]
    text = pyperclip.paste()

    if option == '-h':
        print_help()
    elif option == '-w':
        count_words(text)
    elif option == '-c':
        count_characters(text)
    elif option == '-i':
        count_individual_characters(text)
    else:
        print("Error: Unknown option.")
        print_help()

if __name__ == "__main__":
    main()
