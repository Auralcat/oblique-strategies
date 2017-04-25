#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""Quick and dirty script to join different parts of text files.
 Adds only unique lines to the final file."""

import os

# Putting everything into a set ensures you get unique lines.
line_set = set()

# Reading the file paths and the files' content
for textfile in os.listdir(os.getcwd()):
    if textfile.endswith('.txt'):
        with open(textfile, 'r') as f:
            print("Opening file %s" % f)
            for l in f.readlines():
                line_set.add(l)

# Here's how we'll flatten the sublists, that is, join everything into a
# single big list:
strats = [item for sublist in line_set for item in sublist]

# Writing the files' content to a single joined file
with open("./joined_files.txt", 'w') as output_file:
    for line in strats:
        output_file.write(line)

print("Files joined.")
