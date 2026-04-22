#!/usr/bin/env python3

import re

def search(file = 'origin.txt', pattern=r'\w*herit\w*', output_file='Inheritance_Output.txt'):
    """
    Searches a text file for words matching a given regular expression and writes
    each match along with its line number to a specified output file.

    Args:
        file (str): Path to the input text file. Defaults to 'origin.txt'.
        pattern (str): Regular expression pattern to search for. Defaults to r'\w*herit\w*'.
        output_file (str): Path to the output file. Defaults to 'Inheritance_Output.txt'.

    Returns:
        int: The total number of matches found.
    """
    occurrences = 0
    herit_pattern = re.compile(pattern, re.IGNORECASE)
    #Chuckie D
    print(f"Opening {file}")
    with open(file, 'r') as input:
        print(f"Opening {output_file}")
        with open(output_file, 'w') as output:
            for line_index, line in enumerate(input):
                for match_object in herit_pattern.finditer(line):
                    occurrences += 1
                    output.write("{line_number}\t{object}\n".format(line_number = line_index +1, object = match_object.group()))


    print("Done!")
    print(f"{file} is closed?", input.closed)
    print(f"{output_file} is closed?", output.closed)
    return occurrences


if __name__ == "__main__":
    main()
