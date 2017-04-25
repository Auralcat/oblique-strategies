#/usr/bin/python3
# -*- encoding: utf-8 -*-

"""Oblique Strategies for the command line
   Just run the script and it returns a card."""

import random

def getStrategies():
    with open("/home/lucas/oblique-strategies/src/joined_files.txt") as f:
        strategies = [line.strip('\n') for line in f.readlines()]
    return strategies

def callStrategy():
    print(random.choice(getStrategies()))

callStrategy()
