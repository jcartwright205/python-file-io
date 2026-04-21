#!/usr/bin/env python3

import re

def inheritance(file = 'origin.txt'):
    """
    Searches a text file for words containing 'herit' (case-insensitive) and writes
    each match along with its line number to 'Inheritance_Output.txt'.

    Args:
        file (str): Path to the input text file. Defaults to 'origin.txt'.

    Returns:
        int: The total number of matches found.
    """
    occurrences = 0
    herit_pattern_string = r'\w*herit\w*'
    herit_pattern = re.compile(herit_pattern_string, re.IGNORECASE)
    #Chuckie D
    print("Opening On the Origin of Species")
    with open(file, 'r') as input:
        print("Opening Inheritance_Output.txt")
        with open('Inheritance_Output.txt', 'w') as output:
            for line_index, line in enumerate(input):
                for match_object in herit_pattern.finditer(line):
                    occurrences += 1
                    output.write("{line_number}\t{object}\n".format(line_number = line_index +1, object = match_object.group()))
    return occurrences


if __name__ == "__main__":
    main()
