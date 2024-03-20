# PyWordCounter Script Documentation
## Overview

    The PyWordCounter script is an efficient Python utility crafted to analyze the content of your system's clipboard, focusing on text analysis through various metrics. It employs the pyperclip module to fetch text data directly from the clipboard and utilizes Python's built-in pprint module to neatly display the analysis results. The script also integrates a custom helper module designed to furnish users with helpful instructions on utilizing the script effectively. This tool is perfect for users seeking quick insights into the text data they work with, including word counts, character frequency analysis, and total character counts, emphasizing ease of use and accessibility.

## Dependencies

    To ensure smooth operation of the PyWordCounter script, the following dependencies must be met:

        Python: The script is compatible with Python 3.x. Ensure that Python 3 is installed on your system.
        pyperclip: This third-party module enables the script to access and manipulate the system's clipboard content. It is not included with Python and requires separate installation.

## Installation
### Prerequisites

    Before proceeding with the installation, confirm that Python 3.x is installed on your system by running python --version or python3 --version in your terminal or command prompt.

### Installing Dependencies

        Install the pyperclip module using pip, Python's package installer. Open your terminal or command prompt and execute the following command:

            pip install pyperclip

### Making the Script Globally Executable

To use the PyWordCounter script from any location on your system, follow these steps to make it globally executable:

    Make the Script Executable: Modify the script's first line to #!/usr/bin/env python3 to ensure it uses the correct Python interpreter. Then, set the script file's execution permissions with the command:

        chmod +x PyWordCounter.py

    Move the Script to a Global Location: Move your script to a directory that is included in your system's PATH environment variable. A common choice is /usr/local/bin for Linux and macOS systems:

        mv PyWordCounter.py /usr/local/bin/pywordcounter

This command renames the script to pywordcounter and moves it to a global location. Adjust the command according to your preferred naming convention and applicable directory for your operating system.

    Verify Installation: Ensure that the script is correctly installed and accessible from any directory by typing pywordcounter -h in your terminal. This should display the help documentation of the script.

## Usage

The PyWordCounter script is invoked from the command line, accompanied by an option to specify the desired analysis operation on the clipboard's text content. The script supports the following options:

    -c: Counts and displays the total number of characters within the ASCII range 97 to 122 (inclusive). Note: The script's logic has been optimized to accurately filter characters based on their ASCII values.
    -i: Analyzes and prints the frequency of each individual character present in the clipboard's text, disregarding case sensitivity.
    -w: Calculates and shows the total number of words in the clipboard's text, where a word is defined as a sequence of characters bounded by whitespace.
    -h: Invokes the helper module to present a detailed guide and explanation of the available commands and their respective functions.

To execute an analysis, first copy the text of interest to your clipboard. Then, run the script with your chosen option from the command line. For instance:

pywordcounter

This command will output the total word count of the currently copied text to your clipboard.
Comprehensive Help Documentation

For detailed instructions or to review the command options available with the PyWordCounter script, execute the script with the -h option. This action will print a comprehensive usage guide, elucidating each option's functionality.
License

The PyWordCounter script is distributed under the terms of the MIT License. It is provided "as is", with no warranty expressed or implied. You are free to modify, distribute, and use the script in any manner, provided that credit is given to the original creator.
