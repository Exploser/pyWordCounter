# PyWordCount Script

## Overview

This Python script is designed to perform text analysis operations on the contents of the clipboard. It includes functions for counting individual characters, total characters, and words within the text. This script makes use of the pyperclip module to access clipboard content and the pprint module for formatted output. It also references a custom module named helper for displaying help information.
Dependencies

    Python: The script is written for Python and should be compatible with Python 3.x versions.
    pyperclip: A module for accessing clipboard content. This needs to be installed separately if not already available.
    pprint: A module for pretty-printing Python data structures, which is part of the Python Standard Library.

## Installation

    Ensure Python 3.x is installed on your system.

    Install the pyperclip module using pip:

        pip install pyperclip

## Usage

The script accepts command-line arguments to specify the operation to perform:

    -c: Count total characters in the clipboard text that are within the ASCII range 97 to 122 (inclusive). Note: There seems to be a logical error in this range check, as it should be and instead of or to accurately filter characters.
    -i: Count the occurrences of each individual character in the clipboard text, ignoring case.
    -w: Count the total number of words in the clipboard text. A word is defined as any sequence of characters separated by whitespace.
    -h: Display help information using a function from an external module named helper.

To use the script, copy some text to the clipboard and run the script with one of the above arguments. For example:

        python script.py -c

This command will print the total character count of the text in the clipboard.
Functions

    idvCharCounter(): Counts and prints the occurrences of each individual character in the clipboard text.
    wordCounter(): Counts and prints the total number of words in the clipboard text.
    totalCharCounter(): Counts and prints the total number of characters in the clipboard text that fall within the ASCII range for letters.
    handler(): Parses command-line arguments and calls the appropriate function based on the argument provided.

## Error Handling

The script includes basic error handling for cases where no arguments are passed or an incorrect usage pattern is detected (such as passing too many arguments). In these cases, it either calls the helper() function from the helper module or prints an error message.
Notes

    The script assumes the presence of a module named helper which contains a function named helper() for displaying help information. This module and function are not defined within the provided script and need to be implemented separately.
    There is a potential logical issue in the totalCharCounter() function's conditional check (ord(char) >= 97 or ord(char) <= 122). To accurately count characters within the ASCII range for lowercase letters, this condition should use and instead of or.

