#!/usr/bin/env python3

import re

if __name__ == "__main__":

    herit_pattern_string = r'\w*herit\w*'
    herit_pattern = re.compile(herit_pattern_string, re.IGNORECASE)
    #Chuckie D
    print("Opening On the Origin of Species")
    with open('origin.txt', 'r') as input:
        print("Opening Inheritance_Output.txt")
        with open('Inheritance_Output.txt') as output:
            for line_index, line in enumerate(input):
                line = line.strip()
                word_list = line.split()
                
